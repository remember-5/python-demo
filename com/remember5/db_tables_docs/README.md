# Install 

`poetry add pymysql pandas openpyxl python-docx sqlparse`

# Usage
 
sql model 

```shell
python main.py sql --sql sql.sql --output output.xlsx
```

db model

```shell
python main.py db --host host --user user --password password --database database --port port --output output.xlsx
```
