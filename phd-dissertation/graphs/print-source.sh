#!/bin/bash                                                                                                                                                            

#set -x -v

function print_lines {

    date=$1
    in=$2
    dir=$3
    name=$4

    cd $in
    hash=$(git rev-list master -n 1 --first-parent --before=$1)

    git checkout $hash 2>/dev/null

    lines=$(find $dir -type f -exec wc {} \; | sed s:resources/avro:avro:g | grep -v -e resources -e "hadoop/bam" -e repo | awk '{sum += $1} END {print sum}')
    
    if [[ $? != 0 ]]
    then
	ls
    else
	echo "$name $date $lines"
    fi

    cd ..
}

td=$(mktemp -d bdg-source-XXXX)

cd $td

git clone https://github.com/bigdatagenomics/adam.git
git clone https://github.com/bigdatagenomics/avocado.git
git clone https://github.com/bigdatagenomics/utils.git
git clone https://github.com/bigdatagenomics/bdg-formats.git
git clone https://github.com/bigdatagenomics/cannoli.git

print_lines 2013-05-01 adam src adam-core
print_lines 2013-06-01 adam src adam-core
print_lines 2013-07-01 adam adam-convert adam-core
print_lines 2013-07-01 adam adam-format bdg-formats
print_lines 2013-08-01 adam adam-convert adam-core
print_lines 2013-08-01 adam adam-format bdg-formats
print_lines 2013-09-01 adam adam-convert adam-core
print_lines 2013-09-01 adam adam-format bdg-formats
print_lines 2013-10-01 adam adam-commands adam-core
print_lines 2013-10-01 adam adam-format bdg-formats
print_lines 2013-10-01 avocado src avocado-core
print_lines 2013-11-01 adam adam-commands adam-core
print_lines 2013-11-01 adam adam-format bdg-formats
print_lines 2013-11-01 avocado src avocado-core
print_lines 2013-12-01 adam adam-commands adam-core
print_lines 2013-12-01 adam adam-format bdg-formats
print_lines 2013-12-01 avocado src avocado-core
print_lines 2014-01-01 adam adam-core adam-core
print_lines 2014-01-01 adam adam-cli adam-cli
print_lines 2014-01-01 adam adam-format bdg-formats
print_lines 2014-01-01 avocado src avocado-core
print_lines 2014-02-01 adam adam-core adam-core
print_lines 2014-02-01 adam adam-cli adam-cli
print_lines 2014-02-01 adam adam-format bdg-formats
print_lines 2014-02-01 avocado src avocado-core
print_lines 2014-03-01 adam adam-core adam-core
print_lines 2014-03-01 adam adam-cli adam-cli
print_lines 2014-03-01 adam adam-format bdg-formats
print_lines 2014-03-01 avocado avocado-core avocado-core
print_lines 2014-04-01 adam adam-core adam-core
print_lines 2014-04-01 adam adam-cli adam-cli
print_lines 2014-04-01 adam adam-format bdg-formats
print_lines 2014-04-01 avocado avocado-core avocado-core
print_lines 2014-05-01 adam adam-core adam-core
print_lines 2014-05-01 adam adam-cli adam-cli
print_lines 2014-05-01 adam adam-format bdg-formats
print_lines 2014-05-01 avocado avocado-core avocado-core
print_lines 2014-06-01 adam adam-core adam-core
print_lines 2014-06-01 adam adam-cli adam-cli
print_lines 2014-06-01 adam adam-format bdg-formats
print_lines 2014-06-01 avocado avocado-core avocado-core
print_lines 2014-07-01 adam adam-core adam-core
print_lines 2014-07-01 adam adam-cli adam-cli
print_lines 2014-07-01 bdg-formats src bdg-formats
print_lines 2014-07-01 avocado avocado-core avocado-core
print_lines 2014-08-01 adam adam-core adam-core
print_lines 2014-08-01 adam adam-apis adam-apis
print_lines 2014-08-01 adam adam-cli adam-cli
print_lines 2014-08-01 bdg-formats src bdg-formats
print_lines 2014-08-01 avocado avocado-core avocado-core
print_lines 2014-08-01 avocado avocado-cli avocado-cli
print_lines 2014-08-01 utils . utils
print_lines 2014-09-01 adam adam-core adam-core
print_lines 2014-09-01 adam adam-apis adam-apis
print_lines 2014-09-01 adam adam-cli adam-cli
print_lines 2014-09-01 bdg-formats src bdg-formats
print_lines 2014-09-01 avocado avocado-core avocado-core
print_lines 2014-09-01 avocado avocado-cli avocado-cli
print_lines 2014-09-01 utils . utils
print_lines 2014-10-01 adam adam-core adam-core
print_lines 2014-10-01 adam adam-apis adam-apis
print_lines 2014-10-01 adam adam-cli adam-cli
print_lines 2014-10-01 bdg-formats src bdg-formats
print_lines 2014-10-01 avocado avocado-core avocado-core
print_lines 2014-10-01 avocado avocado-cli avocado-cli
print_lines 2014-10-01 utils . utils
print_lines 2014-11-01 adam adam-core adam-core
print_lines 2014-11-01 adam adam-apis adam-apis
print_lines 2014-11-01 adam adam-cli adam-cli
print_lines 2014-11-01 bdg-formats src bdg-formats
print_lines 2014-11-01 avocado avocado-core avocado-core
print_lines 2014-11-01 avocado avocado-cli avocado-cli
print_lines 2014-11-01 utils . utils
print_lines 2014-12-01 adam adam-core adam-core
print_lines 2014-12-01 adam adam-apis adam-apis
print_lines 2014-12-01 adam adam-cli adam-cli
print_lines 2014-12-01 bdg-formats src bdg-formats
print_lines 2014-12-01 avocado avocado-core avocado-core
print_lines 2014-12-01 avocado avocado-cli avocado-cli
print_lines 2014-12-01 utils . utils
print_lines 2015-01-01 adam adam-core adam-core
print_lines 2015-01-01 adam adam-apis adam-apis
print_lines 2015-01-01 adam adam-cli adam-cli
print_lines 2015-01-01 bdg-formats src bdg-formats
print_lines 2015-01-01 avocado avocado-core avocado-core
print_lines 2015-01-01 avocado avocado-cli avocado-cli
print_lines 2015-01-01 utils . utils
print_lines 2015-02-01 adam adam-core adam-core
print_lines 2015-02-01 adam adam-apis adam-apis
print_lines 2015-02-01 adam adam-cli adam-cli
print_lines 2015-02-01 bdg-formats src bdg-formats
print_lines 2015-02-01 avocado avocado-core avocado-core
print_lines 2015-02-01 avocado avocado-cli avocado-cli
print_lines 2015-02-01 utils . utils
print_lines 2015-03-01 adam adam-core adam-core
print_lines 2015-03-01 adam adam-apis adam-apis
print_lines 2015-03-01 adam adam-cli adam-cli
print_lines 2015-03-01 bdg-formats src bdg-formats
print_lines 2015-03-01 avocado avocado-core avocado-core
print_lines 2015-03-01 avocado avocado-cli avocado-cli
print_lines 2015-03-01 utils . utils
print_lines 2015-04-01 adam adam-core adam-core
print_lines 2015-04-01 adam adam-apis adam-apis
print_lines 2015-04-01 adam adam-cli adam-cli
print_lines 2015-04-01 bdg-formats src bdg-formats
print_lines 2015-04-01 avocado avocado-core avocado-core
print_lines 2015-04-01 avocado avocado-cli avocado-cli
print_lines 2015-04-01 utils . utils
print_lines 2015-05-01 adam adam-core adam-core
print_lines 2015-05-01 adam adam-apis adam-apis
print_lines 2015-05-01 adam adam-cli adam-cli
print_lines 2015-05-01 bdg-formats src bdg-formats
print_lines 2015-05-01 avocado avocado-core avocado-core
print_lines 2015-05-01 avocado avocado-cli avocado-cli
print_lines 2015-05-01 utils . utils
print_lines 2015-06-01 adam adam-core adam-core
print_lines 2015-06-01 adam adam-apis adam-apis
print_lines 2015-06-01 adam adam-cli adam-cli
print_lines 2015-06-01 bdg-formats src bdg-formats
print_lines 2015-06-01 avocado avocado-core avocado-core
print_lines 2015-06-01 avocado avocado-cli avocado-cli
print_lines 2015-06-01 utils . utils
print_lines 2015-07-01 adam adam-core adam-core
print_lines 2015-07-01 adam adam-apis adam-apis
print_lines 2015-07-01 adam adam-cli adam-cli
print_lines 2015-07-01 bdg-formats src bdg-formats
print_lines 2015-07-01 avocado avocado-core avocado-core
print_lines 2015-07-01 avocado avocado-cli avocado-cli
print_lines 2015-07-01 utils . utils
print_lines 2015-08-01 adam adam-core adam-core
print_lines 2015-08-01 adam adam-apis adam-apis
print_lines 2015-08-01 adam adam-cli adam-cli
print_lines 2015-08-01 bdg-formats src bdg-formats
print_lines 2015-08-01 avocado avocado-core avocado-core
print_lines 2015-08-01 avocado avocado-cli avocado-cli
print_lines 2015-08-01 utils . utils
print_lines 2015-09-01 adam adam-core adam-core
print_lines 2015-09-01 adam adam-apis adam-apis
print_lines 2015-09-01 adam adam-cli adam-cli
print_lines 2015-09-01 bdg-formats src bdg-formats
print_lines 2015-09-01 avocado avocado-core avocado-core
print_lines 2015-09-01 avocado avocado-cli avocado-cli
print_lines 2015-09-01 utils . utils
print_lines 2015-10-01 adam adam-core adam-core
print_lines 2015-10-01 adam adam-apis adam-apis
print_lines 2015-10-01 adam adam-cli adam-cli
print_lines 2015-10-01 bdg-formats src bdg-formats
print_lines 2015-10-01 avocado avocado-core avocado-core
print_lines 2015-10-01 avocado avocado-cli avocado-cli
print_lines 2015-10-01 utils . utils
print_lines 2015-11-01 adam adam-core adam-core
print_lines 2015-11-01 adam adam-apis adam-apis
print_lines 2015-11-01 adam adam-cli adam-cli
print_lines 2015-11-01 bdg-formats src bdg-formats
print_lines 2015-11-01 avocado avocado-core avocado-core
print_lines 2015-11-01 avocado avocado-cli avocado-cli
print_lines 2015-11-01 utils . utils
print_lines 2015-12-01 adam adam-core adam-core
print_lines 2015-12-01 adam adam-apis adam-apis
print_lines 2015-12-01 adam adam-cli adam-cli
print_lines 2015-12-01 bdg-formats src bdg-formats
print_lines 2015-12-01 avocado avocado-core avocado-core
print_lines 2015-12-01 avocado avocado-cli avocado-cli
print_lines 2015-12-01 utils . utils
print_lines 2016-01-01 adam adam-core adam-core
print_lines 2016-01-01 adam adam-apis adam-apis
print_lines 2016-01-01 adam adam-cli adam-cli
print_lines 2016-01-01 bdg-formats src bdg-formats
print_lines 2016-01-01 avocado avocado-core avocado-core
print_lines 2016-01-01 avocado avocado-cli avocado-cli
print_lines 2016-01-01 utils . utils
print_lines 2016-02-01 adam adam-core adam-core
print_lines 2016-02-01 adam adam-apis adam-apis
print_lines 2016-02-01 adam adam-cli adam-cli
print_lines 2016-02-01 bdg-formats src bdg-formats
print_lines 2016-02-01 avocado avocado-core avocado-core
print_lines 2016-02-01 avocado avocado-cli avocado-cli
print_lines 2016-02-01 utils . utils
print_lines 2016-03-01 adam adam-core adam-core
print_lines 2016-03-01 adam adam-apis adam-apis
print_lines 2016-03-01 adam adam-cli adam-cli
print_lines 2016-03-01 bdg-formats src bdg-formats
print_lines 2016-03-01 avocado avocado-core avocado-core
print_lines 2016-03-01 avocado avocado-cli avocado-cli
print_lines 2016-03-01 utils . utils
print_lines 2016-04-01 adam adam-core adam-core
print_lines 2016-04-01 adam adam-apis adam-apis
print_lines 2016-04-01 adam adam-cli adam-cli
print_lines 2016-04-01 bdg-formats src bdg-formats
print_lines 2016-04-01 avocado avocado-core avocado-core
print_lines 2016-04-01 avocado avocado-cli avocado-cli
print_lines 2016-04-01 utils . utils
print_lines 2016-05-01 adam adam-core adam-core
print_lines 2016-05-01 adam adam-apis adam-apis
print_lines 2016-05-01 adam adam-cli adam-cli
print_lines 2016-05-01 bdg-formats src bdg-formats
print_lines 2016-05-01 avocado avocado-core avocado-core
print_lines 2016-05-01 avocado avocado-cli avocado-cli
print_lines 2016-05-01 utils . utils
print_lines 2016-06-01 adam adam-core adam-core
print_lines 2016-06-01 adam adam-apis adam-apis
print_lines 2016-06-01 adam adam-cli adam-cli
print_lines 2016-06-01 bdg-formats src bdg-formats
print_lines 2016-06-01 avocado avocado-core avocado-core
print_lines 2016-06-01 avocado avocado-cli avocado-cli
print_lines 2016-06-01 utils . utils
print_lines 2016-07-01 adam adam-core adam-core
print_lines 2016-07-01 adam adam-apis adam-apis
print_lines 2016-07-01 adam adam-cli adam-cli
print_lines 2016-07-01 bdg-formats src bdg-formats
print_lines 2016-07-01 avocado avocado-core avocado-core
print_lines 2016-07-01 avocado avocado-cli avocado-cli
print_lines 2016-07-01 utils . utils
print_lines 2016-08-01 adam adam-core adam-core
print_lines 2016-08-01 adam adam-apis adam-apis
print_lines 2016-08-01 adam adam-cli adam-cli
print_lines 2016-08-01 bdg-formats src bdg-formats
print_lines 2016-08-01 avocado avocado-core avocado-core
print_lines 2016-08-01 avocado avocado-cli avocado-cli
print_lines 2016-08-01 utils . utils
print_lines 2016-09-01 adam adam-core adam-core
print_lines 2016-09-01 adam adam-apis adam-apis
print_lines 2016-09-01 adam adam-cli adam-cli
print_lines 2016-09-01 bdg-formats src bdg-formats
print_lines 2016-09-01 avocado avocado-core avocado-core
print_lines 2016-09-01 avocado avocado-cli avocado-cli
print_lines 2016-09-01 utils . utils
print_lines 2016-10-01 adam adam-core adam-core
print_lines 2016-10-01 adam adam-apis adam-apis
print_lines 2016-10-01 adam adam-cli adam-cli
print_lines 2016-10-01 bdg-formats src bdg-formats
print_lines 2016-10-01 avocado avocado-core avocado-core
print_lines 2016-10-01 avocado avocado-cli avocado-cli
print_lines 2016-10-01 utils . utils
print_lines 2016-11-01 adam adam-core adam-core
print_lines 2016-11-01 adam adam-apis adam-apis
print_lines 2016-11-01 adam adam-cli adam-cli
print_lines 2016-11-01 bdg-formats src bdg-formats
print_lines 2016-11-01 avocado avocado-core avocado-core
print_lines 2016-11-01 avocado avocado-cli avocado-cli
print_lines 2016-11-01 utils . utils
print_lines 2016-12-01 adam adam-core adam-core
print_lines 2016-12-01 adam adam-apis adam-apis
print_lines 2016-12-01 adam adam-cli adam-cli
print_lines 2016-12-01 bdg-formats src bdg-formats
print_lines 2016-12-01 avocado avocado-core avocado-core
print_lines 2016-12-01 avocado avocado-cli avocado-cli
print_lines 2016-12-01 utils . utils
print_lines 2017-01-01 adam adam-core adam-core
print_lines 2017-01-01 adam adam-apis adam-apis
print_lines 2017-01-01 adam adam-cli adam-cli
print_lines 2017-01-01 bdg-formats src bdg-formats
print_lines 2017-01-01 avocado avocado-core avocado-core
print_lines 2017-01-01 avocado avocado-cli avocado-cli
print_lines 2017-01-01 utils . utils
print_lines 2017-02-01 adam adam-core adam-core
print_lines 2017-02-01 adam adam-apis adam-apis
print_lines 2017-02-01 adam adam-cli adam-cli
print_lines 2017-02-01 bdg-formats src bdg-formats
print_lines 2017-02-01 avocado avocado-core avocado-core
print_lines 2017-02-01 avocado avocado-cli avocado-cli
print_lines 2017-02-01 utils . utils
print_lines 2017-02-01 cannoli . cannoli
print_lines 2017-03-01 adam adam-core adam-core
print_lines 2017-03-01 adam adam-apis adam-apis
print_lines 2017-03-01 adam adam-cli adam-cli
print_lines 2017-03-01 bdg-formats src bdg-formats
print_lines 2017-03-01 avocado avocado-core avocado-core
print_lines 2017-03-01 avocado avocado-cli avocado-cli
print_lines 2017-03-01 utils . utils
print_lines 2017-03-01 cannoli . cannoli
print_lines 2017-04-01 adam adam-core adam-core
print_lines 2017-04-01 adam adam-apis adam-apis
print_lines 2017-04-01 adam adam-cli adam-cli
print_lines 2017-04-01 bdg-formats src bdg-formats
print_lines 2017-04-01 avocado avocado-core avocado-core
print_lines 2017-04-01 avocado avocado-cli avocado-cli
print_lines 2017-04-01 utils . utils
print_lines 2017-04-01 cannoli . cannoli
print_lines 2017-05-01 adam adam-core adam-core
print_lines 2017-05-01 adam adam-apis adam-apis
print_lines 2017-05-01 adam adam-cli adam-cli
print_lines 2017-05-01 bdg-formats src bdg-formats
print_lines 2017-05-01 avocado avocado-core avocado-core
print_lines 2017-05-01 avocado avocado-cli avocado-cli
print_lines 2017-05-01 utils . utils
print_lines 2017-05-01 cannoli . cannoli
print_lines 2017-06-01 adam adam-core adam-core
print_lines 2017-06-01 adam adam-apis adam-apis
print_lines 2017-06-01 adam adam-cli adam-cli
print_lines 2017-06-01 bdg-formats src bdg-formats
print_lines 2017-06-01 avocado avocado-core avocado-core
print_lines 2017-06-01 avocado avocado-cli avocado-cli
print_lines 2017-06-01 utils . utils
print_lines 2017-06-01 cannoli . cannoli
print_lines 2017-07-01 adam adam-core adam-core
print_lines 2017-07-01 adam adam-apis adam-apis
print_lines 2017-07-01 adam adam-cli adam-cli
print_lines 2017-07-01 bdg-formats src bdg-formats
print_lines 2017-07-01 avocado avocado-core avocado-core
print_lines 2017-07-01 avocado avocado-cli avocado-cli
print_lines 2017-07-01 utils . utils
print_lines 2017-07-01 cannoli . cannoli
print_lines 2017-08-01 adam adam-core adam-core
print_lines 2017-08-01 adam adam-apis adam-apis
print_lines 2017-08-01 adam adam-cli adam-cli
print_lines 2017-08-01 adam adam-python adam-python
print_lines 2017-08-01 adam adam-r adam-r
print_lines 2017-08-01 bdg-formats src bdg-formats
print_lines 2017-08-01 avocado avocado-core avocado-core
print_lines 2017-08-01 avocado avocado-cli avocado-cli
print_lines 2017-08-01 utils . utils
print_lines 2017-08-01 cannoli . cannoli
print_lines 2017-09-01 adam adam-core adam-core
print_lines 2017-09-01 adam adam-apis adam-apis
print_lines 2017-09-01 adam adam-cli adam-cli
print_lines 2017-09-01 adam adam-python adam-python
print_lines 2017-09-01 adam adam-r adam-r
print_lines 2017-09-01 bdg-formats src bdg-formats
print_lines 2017-09-01 avocado avocado-core avocado-core
print_lines 2017-09-01 avocado avocado-cli avocado-cli
print_lines 2017-09-01 utils . utils
print_lines 2017-09-01 cannoli . cannoli
print_lines 2017-10-01 adam adam-core adam-core
print_lines 2017-10-01 adam adam-apis adam-apis
print_lines 2017-10-01 adam adam-cli adam-cli
print_lines 2017-10-01 adam adam-python adam-python
print_lines 2017-10-01 adam adam-r adam-r
print_lines 2017-10-01 bdg-formats src bdg-formats
print_lines 2017-10-01 avocado avocado-core avocado-core
print_lines 2017-10-01 avocado avocado-cli avocado-cli
print_lines 2017-10-01 utils . utils
print_lines 2017-10-01 cannoli . cannoli
print_lines 2017-11-01 adam adam-core adam-core
print_lines 2017-11-01 adam adam-apis adam-apis
print_lines 2017-11-01 adam adam-cli adam-cli
print_lines 2017-11-01 adam adam-python adam-python
print_lines 2017-11-01 adam adam-r adam-r
print_lines 2017-11-01 bdg-formats src bdg-formats
print_lines 2017-11-01 avocado avocado-core avocado-core
print_lines 2017-11-01 avocado avocado-cli avocado-cli
print_lines 2017-11-01 utils . utils
print_lines 2017-11-01 cannoli . cannoli

cd ~
rm -rf ${td}
