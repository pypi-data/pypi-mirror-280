pyobject - һ���ṩ����Python�ײ���󹤾ߵ�Python��, ����һЩ��ģ�顣A utility tool with some submodules for operating internal python objects.

������ģ�� Included modules: 
============================

__init__ - ��ӡ��Python����ĸ�������

pyobject.browser - ��ͼ�η�ʽ���Python����

pyobject.code\_ - Python bytecode�Ĳ�������

pyobject.search - ����python����

pyobject.newtypes - ����һЩ�µ�����

pyobj_extension(����) - ����Python�ײ��������, �Լ�����ָ���ģ��, ʹ��C���Ա�д

�����ĺ��� Functions:
=====================

describe(obj, level=0, maxlevel=1, tab=4, verbose=False, file=sys.stdout, mode='w' encoding='utf-8')::

    "����"һ������,����ӡ������ĸ������ԡ�
    ����˵��:
    maxlevel:��ӡ�������ԵĲ�����
    tab:�����Ŀո���,Ĭ��Ϊ4��
    verbose:һ������ֵ,�Ƿ��ӡ����������ⷽ��(��__init__)��
    file:һ�������ļ��Ķ���

browse(object, verbose=False, name='obj')::

    ��ͼ�η�ʽ���һ��Python����
    verbose:��describe��ͬ,�Ƿ��ӡ����������ⷽ��(��__init__)

����browse()��ͼ�ν���������ʾ��

.. image:: https://img-blog.csdnimg.cn/direct/3226cebc991a467f9844a1bafda9209d.png
    :alt: browse��������ͼƬ

objectname(obj)::

    objectname(obj) - ����һ�����������,����xxmodule.xxclass��
    ��:objectname(int) -> 'builtins.int'

bases(obj, level=0, tab=4)::

    bases(obj) - ��ӡ���ö���Ļ���
    tab:�����Ŀո���,Ĭ��Ϊ4��

�������� New Functions:
=======================

make_list(start_obj, recursions=2, all=False)::

    ����һ��������б�, �б������ظ��Ķ���
    start:��ʼ�����Ķ���
    recursion:�ݹ����
    all:�Ƿ񽫶������������(��__init__)�����б�

make_iter(start_obj, recursions=2, all=False)::

    ���ܡ�������make_list��ͬ, ������������, �ҵ������п������ظ��Ķ���

search(obj, start, recursions=3)::

    ��һ����㿪ʼ��������
    obj:�������Ķ���
    start:������
    recursion:�ݹ����

������: ``pyobject.newtypes.Code``
==================================

�÷�\: (�����ʾ���Ǵ�doctest��ժȡ��)::

    >>> def f():print("Hello")
    >>> c=Code.fromfunc(f)
    >>> c.co_consts
    (None, 'Hello')
    >>> c.co_consts=(None, 'Hello World!')
    >>> c.exec()
    Hello World!
    >>>
    >>> import os,pickle
    >>> temp=os.getenv('temp')
    >>> with open(os.path.join(temp,"temp.pkl"),'wb') as f:
    ...     pickle.dump(c,f)
    ... 
    >>> f=open(os.path.join(temp,"temp.pkl"),'rb')
    >>> pickle.load(f).to_func()()
    Hello World!
    >>> 
    >>> c.to_pycfile(os.path.join(temp,"temppyc.pyc"))
    >>> sys.path.append(temp)
    >>> import temppyc
    Hello World!
    >>> Code.from_pycfile(os.path.join(temp,"temppyc.pyc")).exec()
    Hello World!


����ģ��: ``pyobj_extension`` 
=============================

��ģ��ʹ����C���Ա�д����ֱ��ʹ��import pyobj_extension, ����ö���ģ�顣���а����ĺ�������:

convptr(pointer)::

    ������ָ��ת��ΪPython������id()�෴��
	Convert a integer pointer to a Python object,as a reverse of id().

py_decref(object,n)::

	����������ü�����Сn��Decrease the reference count of an object for n.

py_incref(object,n)::

    ����������ü�������n��Increase the reference count of an object for n.

*����: ��ǡ����ʹ������3���������ܵ���Python������*

*Warning:improper using of three functions above may cause Python to crash.*

�汾:1.2.3

������־: 

2024-6-20(v1.2.3):�����˰���testĿ¼�µ�.pyc�ļ��ӿǹ��ߣ���������pyobject.browser�еĶ�����������������ʾ�б���ֵ�����ˡ�ǰ����ˢ��ҳ�棬�Լ��������༭��ɾ����������ԡ�

2022-7-25(v1.2.2):�����˲���Python�ײ��������, �Լ�����ָ���C����ģ��pyobj_extension��

2022-2-2(v1.2.0):�޸���һЩbug,�Ż���searchģ�������; pyobject.code_��������Code��,browser�����ӱ༭���Թ���, ������Code��Ĳ��ԡ�

Դ��:�� https://github.com/qfcy/Python/tree/main/pyobject

���� Author: �߷ֳ��� qq:3076711200

����CSDN��ҳ: https://blog.csdn.net/qfcy\_/