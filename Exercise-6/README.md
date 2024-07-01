# Estarta Python Training-Day 6
File handling in Python is a powerful and versatile tool that can be used to perform a wide range of operations. However, it is important to carefully consider the advantages and disadvantages of file handling when writing Python programs, to ensure that the code is secure, reliable, and performs well.

In this article we will explore Python File Handling, Advantages, Disadvantages and How open, write and append functions works in python file.

Python File Open
Before performing any operation on the file like reading or writing, first, we have to open that file. For this, we should use Python’s inbuilt function open() but at the time of opening, we have to specify the mode, which represents the purpose of the opening file.
f = open(filename, mode)
r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. This mode does not override the existing data, but you can modify the data starting from the beginning of the file.
w+: To write and read data. It overwrites the previous file if one exists, it will truncate the file to zero length or create a file if it does not exist.
a+: To append and read data from the file. It won’t override existing data.

Creating a File using the write() Function
Just like reading a file in Python, there are a number of ways to Writing to file in Python. Let us see how we can write the content of a file using the write() function in Python.

Working in Write Mode
Let’s see how to create a file and how the write mode works.

Saving structured data with json
Strings can easily be written to and read from a file. Numbers take a bit more effort, since the read() method only returns strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation). The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

pickle — Python object serialization¶
The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” [1] or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.

There are fundamental differences between the pickle protocols and JSON (JavaScript Object Notation):

JSON is a text serialization format (it outputs unicode text, although most of the time it is then encoded to utf-8), while pickle is a binary serialization format;

JSON is human-readable, while pickle is not;

JSON is interoperable and widely used outside of the Python ecosystem, while pickle is Python-specific;

JSON, by default, can only represent a subset of the Python built-in types, and no custom classes; pickle can represent an extremely large number of Python types (many of them automatically, by clever usage of Python’s introspection facilities; complex cases can be tackled by implementing specific object APIs);

Unlike pickle, deserializing untrusted JSON does not in itself create an arbitrary code execution vulnerability.

json — JSON encoder and decoder¶

json exposes an API familiar to users of the standard library marshal and pickle modules.

Encoding basic Python object hierarchies:

>>>
import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))
"\"foo\bar"
print(json.dumps('\u1234'))
"\u1234"
print(json.dumps('\\'))
"\\"
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
{"a": 0, "b": 0, "c": 0}
from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
'["streaming API"]'
Compact encoding:

>>>
import json
json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
'[1,2,3,{"4":5,"6":7}]'
Pretty printing:

>>>
import json
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}
Decoding JSON:

>>>
import json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
['foo', {'bar': ['baz', None, 1.0, 2]}]
json.loads('"\\"foo\\bar"')
'"foo\x08ar'
from io import StringIO
io = StringIO('["streaming API"]')
json.load(io)
['streaming API']
Specializing JSON object decoding:

>>>
import json
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct

json.loads('{"__complex__": true, "real": 1, "imag": 2}',
    object_hook=as_complex)
(1+2j)
import decimal
json.loads('1.1', parse_float=decimal.Decimal)
Decimal('1.1')
Extending JSONEncoder:

>>>
import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return super().default(obj)

json.dumps(2 + 1j, cls=ComplexEncoder)
'[2.0, 1.0]'
ComplexEncoder().encode(2 + 1j)
'[2.0, 1.0]'
list(ComplexEncoder().iterencode(2 + 1j))
['[2.0', ', 1.0', ']']
Using json.tool from the shell to validate and pretty-print:

echo '{"json":"obj"}' | python -m json.tool
{
    "json": "obj"
}
echo '{1.2:3.4}' | python -m json.tool
Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

