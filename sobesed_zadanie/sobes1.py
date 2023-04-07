# выбрать из текста слова и выбрать повторющаяся

str_dan=' The C extension interface is specific to CPython, and extension modules do not work on other Python implementations. In many cases, it is possible to avoid writing C extensions and preserve portability to other implementations. For example, if your use case is calling C library functions or system calls, you should consider using the ctypes module or the cffi library rather than writing custom C code. These modules let you write Python code to interface with C code and are more portable between implementations of Python than writing and compiling a C extension module.'
# сосчитать все слова и количества в тексте

def otbor_slov(danoe):
    slovo=''
    list_slov=[]
    str_izm=danoe.replace(',','')\
    .replace('.','')
    for raz_str in str_izm:
        if raz_str==' ':
            slovo=''
        if raz_str != ' ':
            slovo+=raz_str
            list_slov.append(slovo)
    print(list_slov)

otbor_slov(str_dan)


