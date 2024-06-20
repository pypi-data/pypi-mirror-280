# tagging & Index Generating for firm level data with maxcompute

## initialize maxcompute account

- Install Aliyun CLI: [Install guide](https://help.aliyun.com/zh/cli/installation-guide)
- run the aliyun configure command to setup account

``` configure
$ aliyun configure
Configuring profile 'default' ...
Aliyun Access Key ID [None]: <Your AccessKey ID>
Aliyun Access Key Secret [None]: <Your AccessKey Secret>
Default Region Id [None]: cn-zhangjiakou
Default output format [json]: json
Default Language [zh]: zh
```

## define Tags

### add new configs

- by csv, folder should include 3 files:
            - tag_list.csv
            - prefix.csv
            - suffix.csv

```python
from tagging_index.tag_processor import TagProcessor
import os
processor = TagProcessor()
tag_config_folder = os.path.join(os.getcwd(), "tag_config")
processor.append_new_config_csv(tag_config_folder)
```

- by json
  
```python
from tagging_index.tag_processor import TagProcessor
import os
processor = TagProcessor()
tag_config_file = os.path.join(os.getcwd(), "tag_config.json")
processor.append_new_config_json(tag_config_file)
```

### add current config

load existing config from maxcompute or local json file to compare with new config

```python
# load the lastest version from maxcompute
processor.load_current_config()
# load the certain version from maxcompute
processor.load_current_config("202401010111")
```

### validate config

validate and print tag tree

```python
validate_result = processor.validate()
pprint(validate_result)
processor.show_tree(root_tag="tag_value",levels=1)
```

### save config

```python
processor.save_to_json(os.path.join(os.getcwd(), "new_config.json"))
# create and save to a new version in maxcompute
processor.save_to_version()
```

## update tag config for udf resource

```python
from tagging_index.maxcompute.udf_release import UdfRelease

udf = UdfRelease()
# release udf only when _udf module updated.
udf.release_udf()
# default to use lastest version
udf.update_dim_resource(version="")
```

## index generation

please notice you need to update the tagging result in maxcompute before generate index

- define index, refer to [index_tag_schema.json]

```python
from tagging_index.index_generator import DemandIndexGenerator,TalentIndexGenerator
DemandIndexGenerator.get_index_schema()
```

- generate index

```python
demand_index = DemandIndexGenerator("index_tag_definition.json")
talent_index = TalentIndexGenerator("index_tag_definition.json")
# list index code with index type suffix
print(talent_index.index_codes)
# set index range
talent_index.start_year = 2018
talent_index.end_year = 2019
# datasource version
talent_index.tag_udf_version="20240604110353.8@6@6"
# check sql script
print(demand_index.generate_sql(['IT_total']).get('IT_total'))
# generate index data and return dataframe
# talent_index.get_index_data('IT_total')
# generate index data and save in maxcompute, ignore index_codes param to generate all
talent_index.generate_index()
# generate the firm level total count in the datasource
talent_index.generate_index_ttl()
```

- generate panel data from index data and maxtrix varibles
  
```python
from tagging_index.data_generator import PanelDataGenerator, VariableMapOther
from tagging_index.index_generator import DemandIndexGenerator

panel_data = PanelDataGenerator()
# set empty array for all comps
panel_data.comp_ids = ['603893.SH', '300158.SZ', "000001.SZ"]
panel_data.start_year=2019
panel_data.end_year=2020
panel_data.index_version = "<<index_version>>"
# add index
panel_data.add_index('IT_total_T')
panel_data.add_index('IT_total_D')
# add source base index (total count)
panel_data.add_source_base(DemandIndexGenerator,'demand_total')
# add performance matrix
panel_data.add_matrix(code='Y0601b',column_name='emp_no')
panel_data.add_matrix('F100801A', 'mkt_value')
# add additional variable from ods table
basic_info ="(select * from ods_csmar_ipo_cobasic where pt=max_pt('ods_csmar_ipo_cobasic'))"
panel_data.add_other_var(VariableMapOther(
    basic_info
    ,'estbdt'
    ,dim_comp_id='stock_id'
    ,col_comp_id='stkcd'))
print(panel_data.get_panel_sql())
panel_data.get_result_df().tail(500)
panel_data.save_to_csv("panel_data.csv")
```
