Convenience facilities for working with pyobjc (MacOSX Objective C facilities).
See also: https://pyobjc.readthedocs.io/en/latest/index.html

*Latest release 20240622*:
Initial PyPI release supporting upcoming cs.app.osx.spaces.

## `apple = <cs.app.osx.objc.AutoBundles object at 0x10c3d3070>`

An object whose attributes autoload `{prefix}{attrname}`.
The default `prefix` is DEFAULT_BUNDLE_ID_PREFIX (`'com.apple.'`).

## Class `AutoBundles`

An object whose attributes autoload `{prefix}{attrname}`.
The default `prefix` is DEFAULT_BUNDLE_ID_PREFIX (`'com.apple.'`).

## Class `Bundle(cs.obj.SingletonMixin)`

Wrapper class for an `NSBundle`.

Instances have the following attributes:
* `_bundle`: the underlying `NSBundle` instance
* `_bundle_id`: the identifier of the underlying bundle, eg `'com.apple.HIServices'`
* `_ns`: a dictionary containing all the functions from the bundle

The functions from the bundle are available as attributes on the `Bundle`.

## Function `cg(func)`

A decorator to provide a `cg_conn` keyword argument if missing,
containing the default Core graphics connection.

Example:

    @cg
    def do_some_graphics(blah, *, cg_conn, ...):
        ...

## Function `convertNSDate(d: objc.NSDate) -> datetime.datetime`

Convert an `NSDate` into a `datetime`.

## Function `convertNSDateComponents(d: objc.NSDateComponents) -> datetime.datetime`

Convert an `NSDateComponents` into a `datetime`.

## Function `convertObjCtype(o)`

Convert an object containing an ObjC object
into the equivalent Python type.

Current conversions:
* `None` -> `None`
* `NSDate`, `NSDateComponents` -> `datetime`
* `ABMultiValueCoreDataWrapper` -> `list` with members converted
* `int` -> `int`
* `objc._pythonify.OC_PythonInt` -> `int`
* `objc._pythonify.OC_PythonFloat` -> float
* dictionries with `.keys()` -> `dict`

# Release Log



*Release 20240622*:
Initial PyPI release supporting upcoming cs.app.osx.spaces.
