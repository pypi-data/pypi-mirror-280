from __future__ import absolute_import, print_function, division

import unittest
import dill
import glob
import os

import numpy as np

from pysaliency.utils import LazyList, TemporaryDirectory, Cache, get_minimal_unique_filenames, atomic_directory_setup, build_padded_2d_array
from test_helpers import TestWithData


def test_minimal_unique_filenames():
    assert get_minimal_unique_filenames(['a/b/c.d']) == ['c.d']

    filenames = [
        'a/b/c/d.e',
        'a/b/c/f.g',
        'a/b/c/h.i',
    ]

    assert get_minimal_unique_filenames(filenames) == ['d.e', 'f.g', 'h.i']

    filenames.append('a/b/C/j.k')
    assert get_minimal_unique_filenames(filenames) == ['c/d.e', 'c/f.g', 'c/h.i', 'C/j.k']


class TestLazyList(TestWithData):
    def test_lazy_list(self):
        calls = []

        def gen(i):
            calls.append(i)
            print('calling with {} yielding {}'.format(i, i**2))
            return i**2

        length = 20

        lazy_list = LazyList(gen, length)
        self.assertEqual(len(lazy_list), length)

        for i in range(length):
            self.assertEqual(lazy_list[i], i**2)

        self.assertEqual(calls, list(range(length)))

    def test_pickle_no_cache(self):
        def gen(i):
            print('calling with {} yielding {}'.format(i, i**2))
            return i**2

        length = 20
        lazy_list = LazyList(gen, length)

        lazy_list = self.pickle_and_reload(lazy_list, pickler=dill)

        self.assertEqual(len(lazy_list._cache), 0)
        self.assertEqual(list(lazy_list), [i**2 for i in range(length)])

    def test_pickle_with_cache(self):
        def gen(i):
            print('calling with {} yielding {}'.format(i, i**2))
            return i**2

        length = 20
        lazy_list = LazyList(gen, length, pickle_cache=True)

        list(lazy_list)  # make sure all list items are generated

        lazy_list = self.pickle_and_reload(lazy_list, pickler=dill)

        self.assertEqual(dict(lazy_list._cache), {i: i**2 for i in range(length)})
        self.assertEqual(list(lazy_list), [i**2 for i in range(length)])


class TestTemporaryDirectory(unittest.TestCase):
    def test_temporary_directory(self):
        with TemporaryDirectory() as tmp_dir:
            self.assertTrue(os.path.isdir(tmp_dir))

        self.assertFalse(os.path.isdir(tmp_dir))
        self.assertFalse(os.path.exists(tmp_dir))


def test_atomic_directory_setup_success(tmp_path):
    directory = tmp_path / 'testdirectory'
    assert not directory.exists()
    with atomic_directory_setup(str(directory)):
        directory.mkdir()
        assert directory.exists()

    assert directory.exists()


def test_atomic_directory_setup_failure(tmp_path):
    directory = tmp_path / 'testdirectory'
    assert not directory.exists()
    try:
        with atomic_directory_setup(str(directory)):
            directory.mkdir()
            assert directory.exists()
            raise ValueError()
    except ValueError:
        pass
    else:
        assert False

    assert not directory.exists()


def test_atomic_directory_setup_success_no_location():
    with atomic_directory_setup(None):
        assert True
    assert True


def test_atomic_directory_setup_failure_no_location():
    try:
        with atomic_directory_setup(None):
            assert True
            raise ValueError()
    except ValueError:
        pass
    else:
        assert False

    assert True


class TestCache(TestWithData):
    def test_basics(self):
        cache = Cache()

        self.assertEqual(len(cache), 0)

        data = np.random.randn(10, 10, 3)
        cache['foo'] = data

        self.assertEqual(list(cache.keys()), ['foo'])
        np.testing.assert_allclose(cache['foo'], data)

        del cache['foo']

        self.assertEqual(len(cache), 0)

    def test_cache_to_disk(self):
        cache = Cache(cache_location=self.data_path)

        self.assertEqual(len(cache), 0)

        data = np.random.randn(10, 10, 3)
        cache['foo'] = data

        self.assertEqual(glob.glob(os.path.join(self.data_path, '*.*')),
                         [os.path.join(self.data_path, 'foo.npy')])

        self.assertEqual(list(cache.keys()), ['foo'])
        np.testing.assert_allclose(cache['foo'], data)

        cache = Cache(cache_location=self.data_path)
        self.assertEqual(cache._cache, {})
        self.assertEqual(list(cache.keys()), ['foo'])
        np.testing.assert_allclose(cache['foo'], data)

        del cache['foo']
        self.assertEqual(len(cache), 0)
        self.assertEqual(glob.glob(os.path.join(self.data_path, '*.*')),
                         [])

    def test_cache_to_disk_nonexisting_location(self):
        cache_location = os.path.join(self.data_path, 'cache')
        cache = Cache(cache_location=cache_location)

        self.assertEqual(len(cache), 0)

        data = np.random.randn(10, 10, 3)
        cache['foo'] = data

        self.assertEqual(glob.glob(os.path.join(cache_location, '*.*')),
                         [os.path.join(cache_location, 'foo.npy')])

        self.assertEqual(list(cache.keys()), ['foo'])
        np.testing.assert_allclose(cache['foo'], data)

        cache = Cache(cache_location=cache_location)
        self.assertEqual(cache._cache, {})
        self.assertEqual(list(cache.keys()), ['foo'])
        np.testing.assert_allclose(cache['foo'], data)

        del cache['foo']
        self.assertEqual(len(cache), 0)
        self.assertEqual(glob.glob(os.path.join(cache_location, '*.*')),
                         [])

    def test_pickle_cache(self):
        cache = Cache()

        self.assertEqual(len(cache), 0)

        data = np.random.randn(10, 10, 3)
        cache['foo'] = data

        self.assertEqual(list(cache.keys()), ['foo'])
        np.testing.assert_allclose(cache['foo'], data)

        cache2 = self.pickle_and_reload(cache)
        self.assertEqual(cache2._cache, {})
        self.assertEqual(len(cache2), 0)

    def test_pickle_cache_with_location(self):
        cache = Cache(cache_location=self.data_path)

        self.assertEqual(len(cache), 0)

        data = np.random.randn(10, 10, 3)
        cache['foo'] = data

        self.assertEqual(glob.glob(os.path.join(self.data_path, '*.*')),
                         [os.path.join(self.data_path, 'foo.npy')])

        self.assertEqual(list(cache.keys()), ['foo'])
        np.testing.assert_allclose(cache['foo'], data)

        cache2 = self.pickle_and_reload(cache)
        self.assertEqual(cache2._cache, {})
        self.assertEqual(len(cache2), 1)
        np.testing.assert_allclose(cache2['foo'], data)


def test_build_padded_2d_array():
    arrays = [
        [0.1, 1, 2],
        [0, 1],
        [0, 1, 2, 4],
        [0, 3]
    ]

    expected = np.array([
        [0.1, 1, 2, np.nan],
        [0, 1, np.nan, np.nan],
        [0, 1, 2, 4],
        [0, 3, np.nan, np.nan]
    ])
    actual = build_padded_2d_array(arrays)

    np.testing.assert_allclose(actual, expected)

    expected = np.hstack((actual, np.ones((4, 1)) * np.nan))
    actual = build_padded_2d_array(arrays, max_length=5)
    np.testing.assert_allclose(actual, expected)


if __name__ == '__main__':
    unittest.main()
