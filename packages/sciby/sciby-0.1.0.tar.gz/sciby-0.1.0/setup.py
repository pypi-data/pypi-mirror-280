# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:36:58 2017

@author: a
"""
package='sciby'#包名,需与文件夹名一致
version='0.1.0'
#buildpy 需要编译为.c的.py文件，需明确列出文件名，否则打包wheel时无法定位ext_modules
#buildpy=['elect/test.py']
buildpy=[
"sciby/calc_expr.py",
"sciby/process.py",
"sciby/service.py",
"sciby/algorithm/weight.py",
"sciby/algorithm/binning.py",
"sciby/algorithm/correlate.py",
"sciby/algorithm/distance.py",
"sciby/algorithm/entropy.py",
"sciby/algorithm/gene.py",
"sciby/algorithm/kdtree.py",
"sciby/algorithm/linear_regression.py",
"sciby/algorithm/metric.py",
"sciby/algorithm/pca.py",
"sciby/algorithm/similar.py",
"sciby/algorithm/trie.py",
"sciby/associate/apriori.py",
"sciby/associate/rule_merge.py",
"sciby/associate/sbar.py",
"sciby/cluster/bestkmeans.py",
"sciby/cluster/fourstep.py",
"sciby/cluster/seqsim.py",
"sciby/graph/louvain.py",
"sciby/image/assess.py",
"sciby/image/edge.py",
"sciby/image/feature.py",
"sciby/image/kernel.py",
"sciby/image/process.py",
"sciby/image/threshold.py",
"sciby/language/cut.py",
"sciby/language/document.py",
"sciby/language/entity.py",
"sciby/language/hash.py",
"sciby/language/keyword.py",
"sciby/language/longest_common.py",
"sciby/language/process.py",
"sciby/language/tagging.py",
"sciby/language/tokenize.py",
"sciby/language/topic.py",
"sciby/language/vocab.py",
"sciby/neuralnet/utils.py",
"sciby/neuralnet/activate.py",
"sciby/neuralnet/attention.py",
"sciby/neuralnet/bert.py",
"sciby/neuralnet/crf.py",
"sciby/neuralnet/dataset.py",
"sciby/neuralnet/dropout.py",
"sciby/neuralnet/esim.py",
"sciby/neuralnet/function.py",
"sciby/neuralnet/glove.py",
"sciby/neuralnet/hypernet.py",
"sciby/neuralnet/lora.py",
"sciby/neuralnet/loss.py",
"sciby/neuralnet/lstm.py",
"sciby/neuralnet/lstm_crf.py",
"sciby/neuralnet/mask_linear.py",
"sciby/neuralnet/optimize.py",
"sciby/neuralnet/prepare.py",
"sciby/neuralnet/resnet.py",
"sciby/neuralnet/skip_gram.py",
"sciby/neuralnet/train.py",
"sciby/neuralnet/transformer.py",
"sciby/timeseries/filter.py",
"sciby/timeseries/outlier.py",
"sciby/timeseries/segment.py"
    ]
#include 需要复制tar.gz包中的资源文件或文件夹，必须是tar.gz中包含的资源
#include=['elect/data','elect/pkgs/jieba/analyse/idf.txt','elect/pkgs']
include=['sciby/data']
#exclude 需要排除的文件或文件夹，
#exclude=['elect/apps','elect/guard.py','elect/data/brand.json','elect/pkgs']+[package+'/nltk/'+i for i in os.listdir(package+'/nltk') if i.endswith('.py') and i.startswith('__') and i not in ['__init__.py']]
import os
exclude=[]+sum([[os.path.join(dirpath,f) for f in filenames if f.startswith('__') and f.endswith('.py') and f not in ['__init__.py']] for dirpath,_,filenames in os.walk(package)],[])
#include和exclude同时存在的内容，会exclude



#setup
keywords = ()
description = ""
long_description = ""#如果有README.md，该项会被README.md内容覆盖
url = ""
author = ""
author_email = ""
license = "Licence"
platforms = "any"
install_requires = ['numpy>=1.24.0', 'scipy>=1.12.0', 'pandas>=2.2.0']#,'torch>=2.2.0']
#%%以下内容不可修改
import os,io
import sys
from setuptools import setup

#路径分隔符统一
include=[i.replace('\\','/') for i in include]
exclude=[i.replace('\\','/') for i in exclude]
buildpy=[i.replace('\\','/') for i in buildpy]

#README.md
if os.path.exists('README.md'):
    with io.open('README.md',encoding='utf-8') as f:
        long_description = f.read()

#生成MANIFEST.in
with open('MANIFEST.in','w') as f:
    for i in include:
        if os.path.isdir(i):
            f.write('recursive-include %s *\n'%i)
        if os.path.isfile(i):
            f.write('include %s\n'%i)
    for i in exclude:
        if os.path.isdir(i):
            f.write('recursive-exclude %s *\n'%i)
        if os.path.isfile(i):
            f.write('exclude %s\n'%i)

ext_modules=[]
if sys.argv[1] in ('sdist'):
    import re
    from Cython.Build import cythonize
    
    for i in buildpy:
        #如果.c已存在,删除
        if os.path.exists(i.replace('.py','.c')):
            os.remove(i.replace('.py','.c'))
        #将build_py编译为.c
        ext_modules+=cythonize(i)
    #clear comment
    expr=re.compile(r'/\*.*?\*/',re.S) 
    for m in ext_modules:
        for s in m.sources:
            with open(s) as f:
                text=f.read()
            text=re.sub(expr,'',text)
            with open(s,'w') as f:
                f.write(text)
else:# sys.argv[1] in ('build','bdist','build_ext',None,'install','develop','bdist_egg','bdist_wheel','register','upload'):
    from setuptools import Extension
    for i in buildpy:
        ext_modules.append(Extension(i.replace('.py','').replace('/','.'),sources=[i.replace('.py','.c')]))

#py_modules排除exclude文件夹、include文件夹
py_modules=[(dirpath,[i for i in dirnames if os.path.join(dirpath,i).replace('\\','/') not in exclude
                     and os.path.join(dirpath,i).replace('\\','/') not in include],filenames)
           for dirpath, dirnames, filenames in os.walk(package) if dirpath.replace('\\','/') not in exclude
           and dirpath.replace('\\','/') not in include]
#py_modules所有py文件
py_modules=sum([[os.path.join(dirpath,i).replace('\\','/') for i in filenames if i.endswith('.py')]
               for dirpath, _, filenames in py_modules],[])
#py_modules排除exclude文件、include文件、buildpy文件
py_modules=[i for i in py_modules if i not in exclude+include+buildpy]

setup(
    name = package,
    version = version,
    keywords = keywords,
    description = description,  
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = url,  
    author = author,
    author_email = author_email,
    license = license,
    platforms = platforms,
    install_requires = install_requires,
    #打包范围
    py_modules=[i.replace('.py','') for i in py_modules],
    ext_modules=ext_modules,
    #没有packages、include_package_data，不影响打包tar.gz，但是打包whl会缺少include
    packages=[i.replace('/','.') for i in include if os.path.isdir(i)],
    include_package_data = True,
    )

#删除MANIFEST.in、.c、.egg-info
if sys.argv[1] in ('sdist'):
    os.remove('MANIFEST.in')
    for m in ext_modules:
        for s in m.sources:
            os.remove(s)
    for i in os.listdir(package+'.egg-info'):
        os.remove(package+'.egg-info/'+i)
    os.rmdir(package+'.egg-info')
