search-file - *A python module providing tools for searching files(or directories).*
һ�����������ļ����ļ��е�Pythonģ�顣

:�����ĺ��� FUNCTIONS:

:directories(path):

- һ��������, �г�path�µ�������Ŀ¼���ļ�����
- ��:

.. code-block:: python

    >>> from search_file import directories
    >>> list(directories("C:"))
    ['C:\\Users',  #��һ��Ŀ¼
    'C:\\Users\\Administrator', #�ڶ���Ŀ¼
    ...,
    'C:\\Windows',
    'C:\\Windows\\System32',
    ...]

dirs: �Ƿ��г�Ŀ¼
files: �Ƿ��г��ļ�

:search(filename,path,minsize=0,maxsize=None):

- һ��������,��path������һ���ļ����ļ��С�
- ��:

.. code-block:: python

    >>> from search_file import search
    >>> list(search("cmd.exe","C:"))
    ['C:\\Windows\\System32\\cmd.exe',
    ...]

:�汾 VERSION:

 1.2.3

Դ����:https://github.com/qfcy/Python/blob/main/search_file.py

�������(2022-2):�����˶�����Գ���

����:*�߷ֳ��� qq:3076711200* �ٶ������˺�:qfcy\_

����CSDN��ҳ: https://blog.csdn.net/qfcy\_/