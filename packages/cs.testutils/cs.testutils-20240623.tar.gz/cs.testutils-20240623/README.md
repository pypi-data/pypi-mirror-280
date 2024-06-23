Hacks to assist with testing.

*Latest release 20240623*:
New assertSingleThread() function to check that there are no left over Threads.

## Function `assertSingleThread(include_daemon=False)`

Test that the is only one `Thread` still running.

## Function `product_test(*da, **dkw)`

Decorator for test methods which should run subTests
against the Cartesian products from `params`.

A specific TestCase would define its own decorator
and apply it throughout the suite.
Here is an example from cs.vt.datadir_tests:

  def multitest(test_method):
    return product_test(
        test_method,
        datadirclass=[DataDir, RawDataDir],
        indexclass=[
            indexclass_by_name(indexname)
            for indexname in sorted(indexclass_names())
        ],
        hashclass=[
            HASHCLASS_BY_NAME[hashname]
            for hashname in sorted(HASHCLASS_BY_NAME.keys())
        ],
    )

whose test suite then just decorates each method with `@multitest`:

    @multitest
    def test000IndexEntry(self):
        ....

Note that because there must be setup and teardown for each product,
the TestCase class may well have empty `setUp` and `tearDown` methods
and instead is expected to provide:
* `product_setup(self,**params)`:
  a setup method taking keyword arguments for each product
* `product_teardown(self)`:
  the corresponding testdown method
There are called around each `subTest`.

## Class `SetupTeardownMixin`

A mixin to support a single `setupTeardown()` context manager method.

*Method `SetupTeardownMixin.setUp(self)`*:
Run `super().setUp()` then the set up step of `self.setupTeardown()`.

*Method `SetupTeardownMixin.tearDown(self)`*:
Run the tear down step of `self.setupTeardown()`,
then `super().tearDown()`.

# Release Log



*Release 20240623*:
New assertSingleThread() function to check that there are no left over Threads.

*Release 20230109*:
* @product_test decorator for running test matrices.
* SetupTeardownMixin providing unittest setUp/tearDown from setupTeardown context manager method.
