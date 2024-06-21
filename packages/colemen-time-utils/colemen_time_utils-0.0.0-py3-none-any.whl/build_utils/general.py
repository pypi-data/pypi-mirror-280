# pylint: disable=deprecated-method
# pylint: disable=no-value-for-parameter
'''
    Description

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 02-24-2023 06:04:49
    `name`: general
    * @TODO []: documentation for general
'''





import base64
import time
import json
import hashlib
from datetime import timezone
from datetime import datetime,date
from threading import Thread
import importlib
import json
import os
from pathlib import PurePath
import re
from string import Template
import subprocess
import sys
from typing import Union,Iterable

from importlib.machinery import SourceFileLoader
# import colemen_utils as c
# import colemen_utilities.string_utils as _csu
# import colemen_utilities.directory_utils as _cdir
# import colemen_utilities.file_utils as _f
# import colemen_utilities.list_utils as _arr


_GET_DATA_INCLUDE_DEFAULT_VALUE = ['file_name', 'extension', 'name_no_ext', 'dir_path', 'access_time', 'modified_time', 'created_time', 'size']

def strip_excessive_chars(value:str,chars:Union[str,list])->str:
    '''
        Removes excessive (2 or more consecutive) chars from the string.

        ----------

        Arguments
        -------------------------
        `value` {str}
            The string to format.
        `chars` {str|list}
            The chars to remove if they occur excessively.

        Return {str}
        ----------------------
        The formatted string

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 06-03-2022 11:47:37
        `memberOf`: string_format
        `version`: 1.0
        `method_name`: strip_excessive_chars
    '''
    if isinstance(chars,(str)):
        chars = [chars]
    for c in chars:
        if c == " ":
            value = re.sub(r'[\s]{2,}',' ',value)
            value = re.sub(r',\s*,',', ',value)
            continue
        reg_c = escape_regex(c)
        exp = rf"[{reg_c}]{{2,}}"
        # print(exp)
        reg = re.compile(exp)
        value = re.sub(reg, c, value)
    return value

def strip(value:str,chars:list,side='both'):
    '''
        Strips characters/strings from the beginning,end or both sides of a string.

        ----------

        Arguments
        -------------------------
        `value` {str}
            The value to be formatted

        `chars` {list}
            A list of strings to be stripped from the value

        [`side`='both'] {str}
            Can be "left", "right", "both"

        Return {str}
        ----------------------
        The formatted value.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 02-04-2022 10:25:04
        `memberOf`: string_format
        `version`: 1.0
        `method_name`: strip_any
    '''
    new_value = value
    cycle = True
    if side in ["both","left"]:
        cycle = True
        while cycle is True:
            matchFound = False
            for char in chars:
                if new_value.startswith(char):
                    new_value = new_value[len(char):]
                    matchFound = True
                else:
                    continue
            if matchFound is False:
                cycle = False
    if side in ["both","right"]:
        cycle = True
        while cycle is True:
            matchFound = False
            for char in chars:
                if new_value.endswith(char):
                    new_value = new_value[:-len(char)]
                    matchFound = True
                else:
                    continue
            if matchFound is False:
                cycle = False
    return new_value

def escape_regex(value:str)->str:
    '''
        Escapes regex special characters.

        ----------

        Arguments
        -------------------------
        `value` {str}
            The string to escape.

        Return {str}
        ----------------------
        The formatted string.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-09-2021 08:46:32
        `memberOf`: string_format
        `version`: 1.0
        `method_name`: escape_regex
    '''
    regex_chars = ["\\", "^", "$", "{", "}", "[", "]", "(", ")", ".", "*", "+", "?", "<", ">", "-", "&"]
    for char in regex_chars:
        value = value.replace(char, f"\\{char}")
    return value

def to_snake_case(subject:str,first_char_alpha=False)->str:
    '''
        Convert a subject to snake_case.

        ----------

        Arguments
        -----------------
        `subject` {str}
            The subject to convert

        [`first_char_alpha`=False] {bool}
            If True any leading non-alphabetic characters will be removed.

        Return
        ----------
        `return` {str}
            The subject converted to snake_case

        Example
        ----------
        BeepBoop Bleep blorp => beep_boop_bleep_blorp
    '''
    subject = str(subject)

    if first_char_alpha:
        subject = re.sub(r'^[^a-zA-Z]*',"",subject)

    subject = re.sub(r'[^a-zA-Z0-9_\s]'," ",subject)
    subject = re.sub(r'(\s|_)+',"_",subject)
    subject = re.sub(r'([a-z])(?:\s|_)?([A-Z])',r"\1_\2",subject)
    return subject.lower()

def to_screaming_snake(subject:str):
    '''
        Convert a subject to SCREAMING_SNAKE_CASE.

        ----------

        Arguments
        -----------------
        `subject` {str}
            The subject to convert

        Return
        ----------
        `return` {str}
            The subject converted to SCREAMING_SNAKE_CASE

        Example
        ----------
        BeepBoop Bleep blorp => BEEP_BOOP_BLEEP_BLORP
    '''

    return to_snake_case(subject).upper()


def array_in_string(array, value, default=False)->bool:
    '''
        iterates the array provided checking if any element exists in the value.

        ----------

        Arguments
        -------------------------
        `array` {list}
            The list of terms to search for in the value.
        `value` {str}
            The string to search within
        [`default`=False] {mixed}
            The default value to return if no match is found.

        Return {mixed}
        ----------------------
        True if a match is found, returns the default value otherwise.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-19-2021 13:54:36
        `memberOf`: parse_utils
        `version`: 1.0
        `method_name`: array_in_string
    '''
    if len(array) == 0:
        return default
    if isinstance(value, (str)) is False:
        print('Second argument of array_in_string, must be a string.')
        print(value)
        return default
    for item in array:
        if item in value:
            return True
    return default

def to_hash(value):
    '''
        Generates a sha256 hash from the string provided.

        ----------
        Arguments
        -----------------
        `value` {str}
            The string to calculate the hash on.

        Return
        ----------
        `return` {str}
            The sha256 hash
    '''
    json_str = json.dumps(value).encode('utf-8')
    hex_dig = hashlib.sha256(json_str).hexdigest()
    return hex_dig

def force_list(value,allow_nulls=True)->list:
    '''
        Confirm that the value is a list, if not wrap it in a list.

        ----------

        Arguments
        -------------------------
        `value` {any}
            The value to test.

        [`allow_nulls`=True] {bool}
            If False and the value is null, the list will be empty.

        Return {list}
        ----------------------
        The value as a list

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 06-03-2022 09:13:57
        `memberOf`: object_utils
        `version`: 1.0
        `method_name`: force_list
        * @xxx [06-03-2022 09:14:52]: documentation for force_list
    '''
    if value is None and allow_nulls is False:
        return []

    if isinstance(value,(tuple)) is True:
        return list(value)
    if isinstance(value,(list)) is False:
        return [value]
    return value

def remove_duplicates(arr:list)->Iterable:
    '''
        Remove duplicate indices from a list.

        ----------

        Arguments
        -------------------------
        `arr` {list}
            The list to filter

        Return {list}
        ----------------------
        The list with duplicates removed.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 07-04-2022 11:07:51
        `memberOf`: list_utils
        `version`: 1.0
        `method_name`: remove_duplicates
        * @xxx [07-04-2022 11:08:44]: documentation for remove_duplicates
    '''


    new_list = []
    for val in arr:
        if val not in new_list:
            new_list.append(val)
    return new_list


def dict_replace_string(value:str,replace:dict):
    '''
        Replace all keys with their values in the value string.

        This replacement method will keep replacing until it finds no matches.
        That essentially means that if a previous replacement changes the value that matches a
        different replacement, it will then replace that value and will continue doing so until
        there are no more matches.

        ----------

        Arguments
        -------------------------
        `value` {string}
            The string to replace values in.

        `replace` {dict}
            The dictionary to use for replacements.

            "find":"replace"


        Return {string|None}
        ----------------------
        The formatted value if successful, None otherwise.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 06-29-2022 05:15:10
        `memberOf`: string_format
        `version`: 1.0
        `method_name`: dict_replace_string
        * @xxx [06-29-2022 05:17:05]: documentation for dict_replace_string
    '''

    if isinstance(replace,(dict)) is False:
        print("The replace argument must be a dictionary","error")
        return None

    match_found = True
    # @Mstep [LOOP] while there are matches still in the value
    while match_found is True:
        match_found = False
        # @Mstep [loop] iterate the replacements
        for k,v in replace.items():
            if v is not None:
                new_val = value.replace(k,v)
                if new_val != value:
                    value = new_val
                    match_found = True
    return value

def dir_exists(path:str):
    value = os.path.isdir(PurePath(path).as_posix())
    return value

def write_file(path:str,contents):
    f = open(path, "w")
    f.write(contents)
    f.close()

def read_file(path:str):
    return open(path, "r")


def as_json(file_path:str):
    '''
        Read a json file into a dictionary.
        strips all comments from file before reading.
    '''
    file_path = PurePath(file_path).as_posix()
    if exists(file_path) is True:
        file_path = file_path.replace("\\", "/")
        file_contents = __parse_json_comments(file_path)
        try:
            return json.loads(file_contents)
        except json.decoder.JSONDecodeError as error:
            error_message = str(error)
            if "decode using utf-8-sig" in error_message:
                decoded_data = file_contents.encode().decode('utf-8-sig')
                return json.loads(decoded_data)

            # json.decoder.JSONDecodeError: Unexpected UTF-8 BOM(decode using utf-8-sig)
    return False

def to_json(file_path, content, indent=4):
    '''
        Write or append to a json file.
        @function to_json

        @param {string} file_path - The path to the file to write.
        @param {mixed} content - The content to be written to the json file
        @param {int} [indent=4] - The pretty print indent setting for the JSON output.
    '''

    json_str = json.dumps(content, indent=indent,default=json_serializer)
    f = open(file_path, "w")
    f.write(json_str)
    f.close()

def json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f'Type {type(obj)} is not serializable')

def __parse_json_comments(file_path:str):
    '''
        strips comments from a json file.

        @return The contents of the file as a string.
    '''
    contents = read_file(file_path)

    contents = re.sub(r'^\s*\/\/[^\n\r]+',"",contents,0,re.MULTILINE)
    # strip multiline comments
    contents = re.sub(r'(\/\*[\s\S]*?\*\/)',"",contents,0,re.MULTILINE)
    return contents


def exists(file_path:str):
    '''
        Confirms that the file exists.

        Arguments
        ----------
        `file_path` {str}
            The file path to test.


        ----------
        `return` {bool}
            True if the file exists, False otherwise.


        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-17-2021 17:15:22
        `memberOf`: file
        `version`: 1.1
        `method_name`: exists


        Changes
        ----------
        12\\17\\2021 17:16:04 - 1.1 - typo on isFile function call.
    '''


    if os.path.isfile(file_path) is True:
        return True
    else:
        return False

def safe_load_json(value,default=False):
    result = False
    try:
        result = json.loads(value)
    except json.decoder.JSONDecodeError:
        # print(e)
        # print(f"    value: {value}")
        return default
    return result

def extension(string:Union[str,list])->Union[str,list]:
    '''
        Formats a file extension to have no leading period.

        ----------

        Arguments
        -------------------------
        `value` {str|list}
            The file extension(s) [separated by commas] or list of extensions to format

        Keyword Arguments
        -------------------------
        `arg_name` {type}
                arg_description

        Return {str}
        ----------------------
        The formatted file extension

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-19-2021 13:33:51
        `memberOf`: string_format
        `version`: 1.0
        `method_name`: extension
    '''
    new_ext_array = []
    if isinstance(string,(str)):
        if "," in string:
            string = string.split(",")
    if isinstance(string, list) is False:
        string = [string]

    for ext in string:
        # print(f"ext: {ext}")
        ext = ext.lower()
        ext = re.sub(r"^\.*", '', ext)
        new_ext_array.append(ext)

    if len(new_ext_array) > 1:
        new_ext_array = list(set(new_ext_array))
    if len(new_ext_array) == 1:
        return new_ext_array[0]
    return new_ext_array

def _gen_extension_array(ext_array):
    # print(f"_gen_extension_array.ext_array: {ext_array}")
    extension_array = []
    if isinstance(ext_array, (str)):
        ext_array = [ext_array]

    for ext in ext_array:
        file_ext = extension(ext)
        extension_array.append(file_ext)

    if len(extension_array) > 1:
        extension_array = list(set(extension_array))
    return extension_array

def get_kwarg(key_name:Union[list,str], default_val=False, value_type=None, **kwargs):
    '''
        Get a kwarg argument that optionally matches a type check or
        return the default value.

        ----------

        Arguments
        -------------------------
        `key_name` {list|string}
            The key name or a list of key names to search kwargs for.

        [`default_val`=False] {any}
            The default value to return if the key is not found or fails
            the type check (if provided.)

        [`value_type`=None] {any}
            The type or tuple of types.
            The kwarg value must match at least one of these.
            Leave as None to ignore type checking.
        `kwargs` {dict}
            The kwargs dictionary to search within.

        Return {any}
        ----------------------
        The value of the kwarg key if it is found.
        The default value if the key is not found or its value fails type checking.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 06-03-2022 08:33:36
        `memberOf`: objectUtils
        `version`: 1.0
        `method_name`: get_kwarg
        * @xxx [06-03-2022 08:38:33]: documentation for get_kwarg
    '''

    kwargs = {k.lower(): v for k, v in kwargs.items()}
    if isinstance(key_name, list) is False:
        key_name = [key_name]

    for name in key_name:
        # generate basic variations of the name
        if value_type is not None:
            if isinstance(kwargs[name], value_type) is True:
                return kwargs[name]
        else:
            return kwargs[name]
    return default_val



def get_modified_time(file_path, ftp=None,rounded:bool=True):
    '''
        get the modified from the file

        ----------

        Arguments
        -------------------------
        `file_path` {string}
            The file to get the modified time from.

        Return {int}
        ----------------------
        The timestamp formatted and rounded.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-13-2021 10:45:32
        `memberOf`: file
        `version`: 1.0
        `method_name`: get_modified_time
    '''
    if ftp is not None:
        return int(datetime.timestamp(datetime.utcfromtimestamp(ftp.path.getmtime(file_path))))

    mod_time = os.path.getmtime(file_path)
    if rounded is True:
        return int(datetime.fromtimestamp(mod_time).replace(tzinfo=timezone.utc).timestamp())
    return mod_time
    # mod_time = int(datetime.fromtimestamp(mod_time).replace(tzinfo=timezone.utc).timestamp())
    # return int(datetime.timestamp(datetime.fromtimestamp(mod_time)))


def get_access_time(file_path,rounded:bool=True):
    '''
        get the access from the file

        ----------

        Arguments
        -------------------------
        `file_path` {string}
            The file to get the access time from.

        Return {int}
        ----------------------
        The timestamp formatted and rounded.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-13-2021 10:45:32
        `memberOf`: file
        `version`: 1.0
        `method_name`: get_modified_time
    '''
    mod_time = os.path.getatime(file_path)
    if rounded is True:
        return int(datetime.fromtimestamp(mod_time).replace(tzinfo=timezone.utc).timestamp())
    return mod_time

def get_create_time(file_path,rounded:bool=True):
    '''
        get the create from the file

        ----------

        Arguments
        -------------------------
        `file_path` {string}
            The file to get the create time from.

        Return {int}
        ----------------------
        The timestamp formatted and rounded.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-13-2021 10:45:32
        `memberOf`: file
        `version`: 1.0
        `method_name`: get_modified_time
    '''
    mod_time = os.path.getctime(file_path)
    if rounded is True:
        return int(datetime.fromtimestamp(mod_time).replace(tzinfo=timezone.utc).timestamp())
    return mod_time

def get_ext(file_path):
    '''
        Get the extension from the file path provided.

        ----------

        Arguments
        -------------------------
        `file_path` {string}
            The file path to be parsed.

        Return {string|boolean}
        ----------------------
        The extension of the file, if it can be parsed, False otherwise.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-13-2021 10:40:21
        `memberOf`: file
        `version`: 1.0
        `method_name`: get_ext
    '''
    file_name = os.path.basename(file_path)
    file_extension = False
    ext = os.path.splitext(file_name)
    if len(ext) == 2:
        file_extension = ext[1]
    return file_extension

def get_name_no_ext(file_path):
    '''
        Get the file name without an extension.

        ----------

        Arguments
        -------------------------
        `file_path` {string}
            The file path to be parsed.

        Return {type}
        ----------------------
        The file name without the extension

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-13-2021 10:38:44
        `memberOf`: file
        `version`: 1.0
        `method_name`: get_name_no_ext
    '''
    value = os.path.basename(file_path).replace(get_ext(file_path), '')
    if value is None:
        value = ""
    return value



def get_data(file_path, **kwargs):
    '''
        Get data associated to the file_path provided.

        ----------

        Arguments
        -----------------
        `file_path`=cwd {str}
            The path to the file.

        Keyword Arguments
        -----------------

            `include`=[] {list}
                A list of keys to include in the returning dictionary.
                This is primarily useful for limiting the time/size of the operation.

        Return
        ----------
        `return` {str}
            A dictionary containing the file's data.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-13-2021 11:02:09
        `memberOf`: file
        `version`: 1.0
        `method_name`: get_data
    '''


    data_include = get_kwarg(['include', "data include"], [], (list, str), **kwargs)
    if isinstance(data_include, (str)):
        data_include = [data_include]
    if len(data_include) == 0:
        data_include = _GET_DATA_INCLUDE_DEFAULT_VALUE
    #file_path = _csu.file_path(file_path)
    file_path = PurePath(file_path).as_posix()
    # print(f"file.get_data.path:{file_path}")
    # exit()
    if exists(file_path):
        # print(f"file exists: {file_path}")
        # print(f"Getting data for file: {file_path}")
        try:
            file_data = {}
            file_data['file_path'] = file_path
            if 'file_name' in data_include:
                file_data['file_name'] = os.path.basename(file_path)
            if 'extension' in data_include:
                file_data['extension'] = get_ext(file_path)
            if 'name_no_ext' in data_include:
                file_data['name_no_ext'] = get_name_no_ext(file_path)
            if 'dir_path' in data_include:
                file_data['dir_path'] = os.path.dirname(file_path)
            if 'access_time' in data_include:
                file_data['access_time'] = get_access_time(file_path)
            if 'modified_time' in data_include:
                file_data['modified_time'] = get_modified_time(file_path)
            if 'created_time' in data_include:
                file_data['created_time'] = get_create_time(file_path)
            if 'size' in data_include:
                file_data['size'] = os.path.getsize(file_path)
            return file_data
        except FileNotFoundError as error:
            print("Error: %s", error)
            return None
    else:
        print("Failed to find the file: %s", file_path)
        return None




class GetFilesThreaded:
    '''
        A class implementation of the get_files method.
        This allows it use threading.
    '''

    def __init__(self, search_path, **kwargs):
        self.threads = []
        self.thread_array = []
        self.file_array = []
        self.max_threads = 20
        self.search_path = search_path
        self.data_include = []

        if search_path is False:
            self.search_path = get_kwarg(['search_path', 'search'], os.getcwd(), (str, list), **kwargs)
        if isinstance(self.search_path, list) is False:
            self.search_path = [self.search_path]

        self.recursive = get_kwarg(['recursive', 'recurse'], True, bool, **kwargs)

        self.data_include = get_kwarg(['data_include'], [], (list, str), **kwargs)
        if isinstance(self.data_include, (str)):
            self.data_include = [self.data_include]

        # ignore_array = get_kwarg(
            # ['ignore', 'ignore_array', 'exclude'], [], (str, list), **kwargs)
        self.exclude = get_kwarg(['exclude', 'ignore', 'ignore array'], [], (list, str), **kwargs)
        if isinstance(self.exclude, (str)):
            self.exclude = [self.exclude]

        self.include = get_kwarg(['include'], [], (list, str), **kwargs)
        if isinstance(self.include, (str)):
            self.include = [self.include]

        self.extension_array = extension(
            get_kwarg(['extensions', 'ext', 'extension'], [], (str, list), **kwargs))
        if isinstance(self.extension_array, (str)):
            self.extension_array = [self.extension_array]

        # self.include_meta_data = get_kwarg(['image meta data', 'meta data','include meta data'], False, bool, **kwargs)
        self.show_index_count = get_kwarg(['show_index_count', 'show count'], True, bool, **kwargs)


    def remove_thread_by_id(self, thread_id):
        '''
            Removes an active thread from self.threads

            ----------

            Arguments
            -------------------------
            `thread_id` {str}
                The id of the thread to remove

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 12-19-2021 13:48:58
            `memberOf`: dir
            `version`: 1.0
            `method_name`: remove_thread_by_id
        '''
        threads = self.threads
        new_threads = []
        for thread in threads:
            if thread != thread_id:
                new_threads.append(thread)
        self.threads = new_threads

    def _get_data_thread(self, file_path):
        # print(f"GetFilesThreaded._get_data_thread.file_path: {file_path}")
        file_data = get_data(file_path, data_include=self.data_include)

        if file_data is not None:
            # ignore = False
            # print(f"file_data['extension']: {file_data['extension']}")
            if len(self.exclude) > 0:
                if array_in_string(self.exclude, file_data['file_path']) is True:
                    return

            if len(self.include) > 0:
                if array_in_string(self.include, file_data['file_path']) is False:
                    return

            if len(self.extension_array) > 0:
                file_ext = extension(file_data['extension'])
                if file_ext not in self.extension_array:
                    return

        self.file_array.append(file_data)
        if self.show_index_count is True:
            print(f"files indexed: {len(self.file_array)}                                             ",end="\r",flush=True)

    def single_file_thread(self, data):
        '''
            Executes the get_data function on an array of files in a separate thread
            and removes itself from self.threads once completed.

            ----------

            Arguments
            -------------------------
            `data` {dict}
                a dictionary containing the file_paths and thread_id keys

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 12-19-2021 13:49:59
            `memberOf`: dir
            `version`: 1.0
            `method_name`: single_file_thread
        '''
        file_paths = data['file_paths']
        for file_path in file_paths:
            self._get_data_thread(file_path)
        self.remove_thread_by_id(data['thread_id'])

    def master(self):
        '''
            Executes the get files process using threads

            ----------

            Return {list}
            ----------------------
            A list of files found in the search_path.

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 12-19-2021 13:52:24
            `memberOf`: dir
            `version`: 1.0
            `method_name`: master
        '''
        # print(f"GetFilesThreaded.master")
        for path in self.search_path:
            # pylint: disable=unused-variable
            for root, folders, files in os.walk(path):

                # print(f"Active Threads: {colemen_utilities.string_format.left_pad(len(self.threads),3,'0')} Total Files: {len(self.file_array)}", end="\r", flush=True)
                while len(self.threads) >= self.max_threads:
                    time.sleep(.1)



                file_paths = [os.path.join(root, x) for x in files]
                data = {
                    "thread_id": to_hash(json.dumps(file_paths)),
                    "file_paths": file_paths
                }
                thread = Thread(target=self.single_file_thread, args=(data,))
                self.threads.append(data['thread_id'])
                self.thread_array.append(thread)
                thread.start()

                if self.recursive is False:
                    break
            # return self.file_array
            # path_files = index_files(path, extension_array, ignore_array, recursive)
            # file_array = path_files + file_array
        # print(f"                                                                                                                      ", end="\r", flush=True)
        for thread in self.thread_array:
            thread.join()

        if self.show_index_count is True:
            print(f"Total Files Indexed: {len(self.file_array)}                                             ")
        return self.file_array



def get_files(
    search_path=False,
    recursive:bool=True,
    exclude:Union[str,list]=None,
    include:Union[str,list]=None,
    extensions:Union[str,list]=None,
    threaded:bool=True,
    show_count:bool=False
    ):
    '''
        Get all files/data from the search_path.

        ----------

        Keyword Arguments
        -----------------
            [`search_path`=cwd] {str|list}
                The search path or list of paths to iterate.

            [`recursive`=True] {boolean}
                If True the path is iterated recursively

            [`exclude`=[]] {str|list}
                A term or list or terms to ignore if the file path contains any of them.

            [`extensions|ext|extension`=[]] {str|list}
                An extension or list of extensions that the file must have.\n
                Can have leading periods or not.\n
                if equal to "images" it will automatically search for these extensions:
                    bmp,dds,dib,eps,gif,icns,ico,im,jpg,jpeg,jpeg 2000,msp,pcx,png,ppm,sgi,spider,tga,tiff,webp,xbm

            [`show_count`=False] {bool}
                If True, the index count is printed to the terminal during indexing.

            [`get_files`=True] {bool}
                if True, this will return a list of dictionaries, otherwise it will return a list of File objects.

            [`threaded`=True] {bool}
                if True, the process is multi-threaded,
                this makes indexing much faster,
                but it can easily overwhelm a cpu depending upon the drive.

            `data_include` {str|list}
                The data to get for each file, the shorter this list the faster it will complete.
                By default it will get this:
                    ['file_name', 'extension', 'name_no_ext', 'dir_path', 'access_time',
                    'modified_time', 'created_time', 'size']

                so the list you provide will limit the amount of
                reading/formatting needed to gather data.

                Example:
                    ['modified_time','size']  will take ~0.000129939 seconds per file on an SSD

                    ['file_name', 'extension', 'name_no_ext', 'dir_path', 'access_time',
                    'modified_time', 'created_time', 'size']

                    will take ~0.000173600 seconds per file on an SSD,
                    it's not much but little things matter.. that's what she said.

            [`ftp`=None] {obj}
                A reference to the ftputil object.

            [`include_meta_data`=False] {bool}
                If True any images that are found will have their meta_data added to the file object.

                Bare in mind that not all images support keywords etc. Currently, only jpg and tiff allow it.


                This will slow things down a bit.

        return
        ----------
        `return` {list}
            A list of dictionaries containing all matching files.
    '''
    file_array = []

    if isinstance(search_path, list) is False:
        search_path = [search_path]

    # threaded = get_kwarg(['threaded', 'thread'], True, bool, **kwargs)
    # recursive = get_kwarg(['recursive', 'recurse'], True, bool, **kwargs)

    # data_include = get_kwarg(['data include'], [], (list, str), **kwargs)
    # if isinstance(data_include, (str)):
        # data_include = [data_include]


    data_include = _GET_DATA_INCLUDE_DEFAULT_VALUE




    # ignore_array = get_kwarg(['ignore', 'ignore_array', 'exclude'], [], (str, list), **kwargs)
    exclude = force_list(exclude,allow_nulls=False)
    # exclude = get_kwarg(['exclude', 'ignore', 'ignore array'], [], (list, str), **kwargs)
    if isinstance(exclude, (str)):
        exclude = [exclude]

    include = force_list(include,allow_nulls=False)
    # include = get_kwarg(['include'], [], (list, str), **kwargs)
    if isinstance(include, (str)):
        include = [include]

    show_index_count = show_count
    # show_index_count = get_kwarg(['show_index_count', 'show count'], False, bool, **kwargs)

    # print(f"file.get_files.kwarg['extension']: ",get_kwarg(['extensions', 'ext', 'extension'], [], (str, list), **kwargs))
    extension_array = force_list(extensions,allow_nulls=False)
    # extension_array = get_kwarg(['extensions', 'ext', 'extension'], [], (str, list), **kwargs)
    # print(f"extension_array - RAW: {extension_array}")
    extension_array = _gen_extension_array(extension_array)
    # print(f"extension_array: {extension_array}")
    # print(f"file.get_files: {search_path}")

    # ftp = get_kwarg(["ftp"], None, None, **kwargs)

    if threaded is True:
        # print(f"file.get_files - Using threads for indexing.")
        for path in search_path:
            gft = GetFilesThreaded(path,
                recursive=recursive,
                exclude=exclude,
                include=include,
                extensions=extension_array,
                show_index_count=show_index_count,
                data_include=_GET_DATA_INCLUDE_DEFAULT_VALUE,
                )
            file_array = gft.master()

            return file_array
    # print(json.dumps(extension_array, indent=4))
    for path in search_path:
        path = PurePath(path).as_posix()
        # pylint: disable=unused-variable
        for root, folders, files in os.walk(path):
            for file in files:
                file_data = get_data(os.path.join(root, file), include=data_include)
                if file_data is not None:
                    # ignore = False
                    # print(f"file_data['extension']: {file_data['extension']}")
                    if len(exclude) > 0:
                        # print(f"filtering excludes")
                        if array_in_string(exclude, file_data['file_path']) is True:
                            continue

                    if len(include) > 0:
                        # print(f"filtering includes")
                        if array_in_string(include, file_data['file_path']) is False:
                            continue

                    if len(extension_array) > 0:
                        # print(f"filtering extension_array")
                        file_ext = extension(file['extension'])
                        if file_ext not in extension_array:
                            continue

                    # if len(ignore_array) > 0:
                    #     for ignore_string in ignore_array:
                    #         if ignore_string in file_data['file_path']:
                    #             ignore = True

                    # if ignore is False:
                        # fd['file_hash'] = generateFileHash(fd['file_path'])
                    # print(f"file found.")
                    file_array.append(file_data)
                    if show_index_count is True:
                        print(f"files indexed: {len(file_array)}                                             ",end="\r",flush=True)
                # else:
                    # print(f"file_data is none")
            if recursive is False:
                # print(f"breaking")
                break

        # path_files = index_files(path, extension_array, ignore_array, recursive)
        # file_array = path_files + file_array

    if show_index_count is True:
        print(f"Total Files Indexed: {len(file_array)}                                             ")

    return file_array




# PATHS = [
#     f"./apricity",
# ]

def list_py_modules(
    root_path:str,
    exclude:Union[str,list]=None,
    additions:Union[str,list]=None,
    print_outputs:bool=False,
    )->Iterable[str]:
    '''
        Compile a list of module import paths for the setuptools setup method.

        ----------

        Arguments
        -------------------------
        `root_name` {str}
            The name of the directory to search in, this must be located in the same directory
            as the setup.py file.

        [`additions`=None] {str,list}
            A list of import paths to add include.
            This where you can imports that are in the root folder of the package (same folder as the setup.py)
            These are added verbatim, so don't fuck up.

        [`exclude`=None] {str,list}
            A list of strings, if any of these are found in a file path, that file will not be included
            __pycache__ directories are always ignored.

        [`print_outputs`=False] {bool}
            If True the imports are printed to console.


        Return {list}
        ----------------------
        A list of import path strings.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 02-24-2023 06:54:02
        `memberOf`: general
        `version`: 1.0
        `method_name`: list_py_modules
        * @xxx [02-24-2023 07:03:03]: documentation for list_py_modules
    '''
    output = []
    root_name = os.path.basename(root_path)
    root_path = os.path.dirname(root_path)

    paths = [f"{root_path}/{root_name}"]
    exclude_base = ['__pycache__',' - Copy']
    if isinstance(exclude,(str)):
        exclude = force_list(exclude,allow_nulls=False)
    exclude_base = exclude_base + [exclude]
    additions = force_list(additions,allow_nulls=False)

    for path in paths:


        path = PurePath(path).as_posix()
        if dir_exists(path) is False:
            if path.startswith("./"):
                test_path = path.replace("./",root_path)
                if dir_exists(test_path):
                    path = test_path
            else:
                continue

        # dir_name = os.path.basename(path)
        files = get_files(path,extensions=['.py'],exclude=['__pycache__'])
        for file in files:

            module_path = f"{root_name}"
            # module_path = f"{root_name}\\{dir_name}"
            # print(f"module_path: {module_path}")
            module_dot_name = f"{root_name}"
            # print(f"module_dot_name: {module_dot_name}")
            file_path = f"{module_path}\\{file.dir_path.replace(path,'')}\\{file.name_no_ext}"
            if file.name == "__init__.py":
                file_path =f"{module_path}\\{file.dir_path.replace(path,'')}"

            dot_name = file_path.replace("\\",".")
            dot_name = strip_excessive_chars(dot_name,["."])
            # dot_name = re.sub(r'[\.]{2,}',".",dot_name)

            if dot_name == f"{module_dot_name}.":
                dot_name = module_dot_name

            output.append(dot_name)

        output = sorted(output)


    output = remove_duplicates(output)
    output = force_list(additions) + output

    if print_outputs:
        for o in output:
            print(f"'{o}',")
    list_path = PurePath(f"{root_path}/package_build_settings.json").as_posix()
    settings = as_json(list_path)
    if settings is not False:
        settings['py_modules'] = output
        to_json(list_path,settings)

    return output

def purge_dist(root_path:str=None):
    '''
        Deletes the dist folder from the project directory.

        ----------


        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-02-2022 08:40:48
        `memberOf`: build_utils
        `version`: 1.0
        `method_name`: purge_dist
        * @xxx [12-02-2022 08:41:15]: documentation for purge_dist
    '''
    if root_path is None:
        root_path = os.getcwd()

    path = f"{root_path}/dist"
    path = PurePath(path).as_posix()
    # print(f"path:{path}")
    if dir_exists(path):
        for f in get_files(path,extensions=['.gz','.whl']):
            # print(f.file_path)
            f.delete()
        # print(f"path exists")
        # _cdir.delete(path)

def create_build_utils_batch(user_name:str=None,password:str=None):
    '''
        Create the build_utils directory and the build_package module.

        Then create the major,minor,patch release batches.

        When you run any of these batch files, they will build the package and optionally
        upload the package to pypi.

        ----------

        Arguments
        -------------------------
        `user_name` {str}
            Pypi user name

        `password` {str}
            pypi password.

        Keyword Arguments
        -------------------------
        `arg_name` {type}
            arg_description

        Return {type}
        ----------------------
        return_description

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 02-25-2023 11:37:42
        `version`: 1.0
        `method_name`: create_build_utils_batch
        * @TODO []: documentation for create_build_utils_batch
    '''
    _confirm_preparations()
    template_path = f"{os.getcwd()}/colemen_utilities/build_utils/build_package.template"
    if exists(template_path) is False:
        template_path = f"{os.getcwd()}/Lib/site-packages/colemen_utilities/build_utils/build_package.template"

    if exists(template_path) is False:
        raise ValueError("Failed to locate the Colemen Utils Template")

    print(f"template_path:{template_path}")
    template = read_file(template_path)
    s = Template(template)
    if user_name is None:
        user_name = "none"
        password = "none"
    else:
        user_name = base64.b64encode(user_name.encode("ascii")).decode("ascii")
        password  = base64.b64encode(password.encode("ascii")).decode("ascii")


    out = s.substitute(
        user_name=user_name,
        password=password,
    )

    utils_path = f"{os.getcwd()}/build_utils"
    build_package_path = f"{utils_path}/build_package.py"
    if dir_exists(utils_path) is False:
        os.mkdir(utils_path)
    write_file(build_package_path,out)
    # _f.write(build_package_path,out)

    module = SourceFileLoader("build_package",build_package_path).load_module()
    module.create_release_batches()

def build_this_package(release:str="patch",user_name:str=None,password:str=None):
    '''
        Build this package's tar file and optionally upload it to pypi.

        ----------

        Arguments
        -------------------------
        `release` {str}
            The release version to increment [major,minor,patch]

        [`user_name`=None] {str}
            Your Pypi user name.

        [`password`=None] {str}
            Your Pypi password.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 02-25-2023 12:39:38
        `memberOf`: general
        `version`: 1.0
        `method_name`: build_this_package
        * @xxx [02-25-2023 12:41:47]: documentation for build_this_package
    '''
    release = release.lower()
    releases = ["major","minor","patch"]
    if release not in releases:
        raise ValueError(f"The release value must be :[{', '.join(releases)}]")
    utils_path = f"{os.getcwd()}/build_utils"
    build_package_path = f"{utils_path}/build_package.py"
    create_build_utils_batch(user_name,password)
    module = SourceFileLoader("build_package",build_package_path).load_module()
    module.main(release)

def _confirm_preparations():
    '''
        Confirm that the setup.py file exists and that wheel twine are installed;
        ----------

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 02-25-2023 12:38:46
        `memberOf`: general
        `version`: 1.0
        `method_name`: _confirm_preparations
        `raises`: TypeError
        * @xxx [02-25-2023 12:39:16]: documentation for _confirm_preparations
    '''
    import importlib.util
    import sys
    setup_path = f"{os.getcwd()}/setup.py"
    if exists(setup_path) is False:
        raise TypeError("Failed to locate the setup.py file.")

    # @Mstep [] install wheel and twine if necessary.
    packages = ["wheel","twine"]
    # print(sys.modules)
    for name in packages:
        is_package_installed(name,auto_install=True)

def install(package):
    '''
        Install a python pip package.
        ----------

        Arguments
        -------------------------
        `package` {str}
            The name of the package to install


        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 02-25-2023 12:38:02
        `version`: 1.0
        `method_name`: install
        * @xxx [02-25-2023 12:38:39]: documentation for install
    '''
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def is_package_installed(package:Union[str,list],auto_install:bool=False,return_missing:bool=True)->Union[list,bool]:
    '''
        Check if a package installed.

        ----------

        Arguments
        -------------------------
        `package` {list,string}
            A package name or list of package names to check on.
        [`auto_install`=False] {bool}
            If True and a package is not installed, it will install it with pip.
        [`return_missing`=True] {bool}
            If True, this will return a list of missing package names, otherwise a boolean


        Return {list,bool}
        ----------------------
        A list of missing packages if `return_missing` is True, a boolean otherwise.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 02-25-2023 12:46:33
        `memberOf`: general
        `version`: 1.0
        `method_name`: is_package_installed
        * @xxx [02-25-2023 12:48:58]: documentation for is_package_installed
    '''
    pkgs = force_list(package,allow_nulls=False)
    missing = []
    for name in pkgs:
        if importlib.util.find_spec(name) is None:
            if auto_install is True:
                install(name)
            else:
                missing.append(name)
    if len(missing) > 0:
        if return_missing is True:
            return missing
        else:
            return False
    return True

def load_module_from_path(name:str,path:str):

    import importlib.util

    # specify the module that needs to be
    # imported relative to the path of the
    # module
    spec=importlib.util.spec_from_file_location(name,path)

    # creates a new module based on spec
    foo = importlib.util.module_from_spec(spec)

    # executes the module in its own namespace
    # when a module is imported or reloaded.
    spec.loader.exec_module(foo)

    return foo

def file_path_to_import_path(path:str,root_path:str=None):
    '''
        Convert a file path to a python import path

        The file should reside in the current working directory, if it does not and the root_path
        is not provided, the result will be practically useless

        Z:\some\file\path\.venv\colemen_utilities\directory_utils\dir_delete.py

        colemen_utilities.directory_utils.dir_delete


        ----------

        Arguments
        -------------------------
        `path` {str}
            The path to the module
        [`root_path`=None] {str}
            The path to the working directory, if not provided the current working directory will be used.

        Return {str}
        ----------------------
        The import path.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 02-27-2023 08:50:49
        `memberOf`: general
        `version`: 1.0
        `method_name`: file_path_to_import_path
        * @xxx [02-27-2023 09:01:32]: documentation for file_path_to_import_path
    '''
    if root_path is None:
        root_path = os.getcwd()
    path = PurePath(path).as_posix()
    # @Mstep [] remove the current working directory from the path.
    path = path.replace(PurePath(root_path).as_posix(),'')
    reps = {
        '/Lib/site-packages/':'',
        '/__init__':'',
        '.py':'',
        '/':'.',
    }
    path = dict_replace_string(path,reps)


    # @Mstep [] remove any leading periods
    import_path = strip(path,["."],"left")
    path = strip_excessive_chars(import_path,["."])


    return import_path

def set_environ(key:str,value):
    if isinstance(value,(str)) is False:
        value = json.dumps(value)
    os.environ[to_screaming_snake(key)] = value


def get_environ(key:str,default=None):
    value = os.environ.get(to_screaming_snake(key))
    if value is None:
        value = default
    else:
        value = safe_load_json(value)
        if value is False:
            value = default

    return value
