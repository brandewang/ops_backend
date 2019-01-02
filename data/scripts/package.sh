#!/bin/bash

app_name=$1
module=$2
app_workspace=$3
package_path=$4
env=$5
type=$6

##日志输出
echo "<<BEGIN>>"

date
cd $app_workspace
mvn install -P $env
if [[ $? != 0 ]];then
	echo "<<END>>"
	exit 1
fi

if [[ $app_name != $module ]];then
	cd $module
fi

if [[ $type == 'tomcat' ]];then
	find target -maxdepth 1  -name "*$module"|xargs -I {} cp -r {} $package_path
elf [[ $type == 'springboot' ]];then
	echo 'haha'
else
	echo "error:unknown type"
	exit 2
fi


echo "<<END>>"
