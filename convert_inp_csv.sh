#!/bin/sh
echo ファイルのパスを入力:
read input_file_name
output_file_name=`date +"%Y%m%d%H%M%S"`
echo $output_file_name
awk 'BEGIN{
		OFS = ","
	}
	{if(($2!~"nan"))
		{print $2, $3>"'"${output_file_name}"'.csv"}
        # 各カラムのx座標とy座標を取り出してくる．
	}' $input_file_name
