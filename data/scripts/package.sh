#!/bin/bash

app_name=$1
module=$2
app_workspace=$3
package_path=$4
env=$5
type=$6

##日志输出
echo "-------BEGIN------"

date
cd $app_workspace
mvn install -P $env
if [[ $? != 0 ]];then
	echo "------END------"
	exit 1
fi

if [[ $app_name != $module ]];then
	cd $module
fi

if [[ $type == 'tomcat' ]];then
	result=(`find target -maxdepth 1  -name "*$module"`)
	result_len=${#result[@]}
	if [[ $result_len != 1 ]];then
		echo 'error: package not found     type:tomcat'
		exit 2
	fi
	cp -r $result  $package_path
elif [[ $type == 'springboot' ]];then
	result=(`find target -maxdepth 1 -name "*$module.[w|j]ar"`)
	result_len=${#result[@]}
	if [[ $result_len != 1 ]];then
		echo 'error: package not found     type:springboot'
		exit 2
	fi
	cp $result $package_path
else
	echo "error:unknown type"
	exit 2
fi


echo "------END------"
