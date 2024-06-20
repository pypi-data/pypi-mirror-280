import pandas as pd 
import os,re,json,logging,datetime
from PIL import Image, ImageDraw
import mysql.connector # pip install mysql-connector-python

class DatabaseQuery:
    def __init__(self, db):
        self.db = db

    def get_table_row(self, table):
        mycursor = self.db.cursor()
        mycursor.execute("SELECT * FROM " + table)
        result = mycursor.fetchall()
        return result

    def get_table_structure(self, table):
        mycursor = self.db.cursor()
        mycursor.execute("SHOW COLUMNS FROM " + table)
        result = [x[0] for x in mycursor.fetchall()]
        return result
    
    def insert_row(self, table, data):
        try:
            mycursor = self.db.cursor()
            if isinstance(data, list):
                columns = ', '.join(data[0].keys())
                values_list = []
                for row_data in data:
                    values = ', '.join([f"'{v}'" for v in row_data.values()])
                    values_list.append(f"({values})")
                values_str = ', '.join(values_list)
            else:
                columns = ', '.join(data.keys())
                values = ', '.join([f"'{v}'" for v in data.values()])
                values_str = f"({values})"
            insert_query = f"INSERT INTO {table} ({columns}) VALUES {values_str}"
            mycursor.execute(insert_query)
            self.db.commit()
            return True
        except Exception as err:
            return str(err)
        

    def delete_row(self, table, condition=None, limit=None):
        try:
            mycursor = self.db.cursor()
            delete_query = f"DELETE FROM {table}"
            if condition:
                delete_query += f" WHERE {condition}"
            if limit:
                delete_query += f" LIMIT {limit}"
            mycursor.execute(delete_query)
            self.db.commit()
            return True
        except Exception as err:
            return str(err)

    def update_row(self, table, update_data, condition=None):
        try:
            mycursor = self.db.cursor()
            set_values = ', '.join([f"{key} = '{value}'" for key, value in update_data.items()])
            update_query = f"UPDATE {table} SET {set_values}"
            if condition:
                update_query += f" WHERE {condition}"
            mycursor.execute(update_query)
            self.db.commit()
            return True
        except Exception as err:
            return str(err)

    def append_value(self, table, column, value_to_append, condition=None):
        try:
            mycursor = self.db.cursor()
            if condition:
                update_query = f"UPDATE {table} SET {column} = CONCAT({column}, '{value_to_append}') WHERE {condition}"
            else:
                update_query = f"UPDATE {table} SET {column} = CONCAT({column}, '{value_to_append}')"
            mycursor.execute(update_query)
            self.db.commit()
            return True
        except mysql.connector.Error as err:
            return str(err)
        
    def exec_query(self,query):
        mycursor = self.db.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    
    def query_data(self, table, select_fields='*', condition=None):
        mycursor = self.db.cursor()
        select_query = f"SELECT {select_fields} FROM {table}"
        if condition:
            select_query += f" WHERE {condition}"
        mycursor.execute(select_query)
        result = mycursor.fetchall()
        return result
    
    def check_table_existence(self,table_name):
        mycursor = self.db.cursor()
        # 执行查询语句检查数据表是否存在
        mycursor.execute("SHOW TABLES LIKE %s", (table_name,))
        result = mycursor.fetchone()
        return bool(result)

    def close_connection(self):
        if self.db:
            self.db.close()

class bbt:
    @staticmethod
    def make(obj_type, *args, **kwargs):
        if obj_type == "DatabaseQuery":
            db = mysql.connector.connect(*args, **kwargs)
            return DatabaseQuery(db)
        # Add more elif conditions for other classes as needed
        else:
            raise ValueError("Invalid object type")
        
# 检查文件夹是否存在，不存在就创建
def check_create_folder(folder_path, create_if_not_exists=True):
    desktop_path = os.path.expanduser("~/Desktop")
    
    # 检查文件夹路径是否为桌面
    if folder_path == desktop_path:
        printLog("文件夹路径为桌面:", folder_path)
        return 2
    
    # 检查文件夹是否存在
    if os.path.exists(folder_path):
        printLog("文件夹存在:", folder_path)
        return folder_path
    
    if create_if_not_exists:
        try:
            os.makedirs(folder_path)
            printLog("文件夹已创建:", folder_path)
            return folder_path
        except OSError as e:
            printLog("创建文件夹时出错:", e)
            return None
    else:
        printLog("文件夹不存在:", folder_path)
        return False

# 记录信息
# logging.info('这是一条信息日志,e,s')
# logging.warning('这是一条警告日志')
# logging.error('这是一条错误日志')
def configure_logging(log_file_path,info):
    # 配置日志记录器
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

    # 记录日志
    logging.info(info)


# 每split_num个结果截取作为df的一行，结果为空的字符串用NA代替
def process_serial_numbers(serial_numbers_positions, extra_param,split_num):
    data = []
    for i in range(0, len(serial_numbers_positions), split_num):
        row_data = []
        for j in range(i, i + split_num):
            if j < len(serial_numbers_positions):
                if len(serial_numbers_positions[j]) > 0:
                    row_data.append(serial_numbers_positions[j][0])
                else:
                    row_data.append('NA')
            else:
                break
                
        # 添加额外参数到每一行
        row_data.append(extra_param)
        
        if len(row_data) == split_num+1:  # 考虑额外参数占一个位置
            data.append(row_data)

    df = pd.DataFrame(data, columns=[f'Column{i+1}' for i in range(split_num)] + ['ExtraParam'])

    return df

# 检查指定文件夹是否包含指定文件
def check_file_in_folder(folder_path, file_name):
    # 获取文件夹中的所有文件列表
    files_in_folder = os.listdir(folder_path)
    
    # 检查指定文件是否在文件列表中
    if file_name in files_in_folder:
        return True
    else:
        return False

# print信息到控制台的同时，输出到log文件    
def printLog(*args, **kwargs):
    log_message = " ".join(map(str, args))  # 将参数转为字符串并拼接
    print(log_message, **kwargs)  # 打印到控制台

    with open('log.log', 'a',encoding='utf-8') as file:
        file.write(str(datetime.datetime.now())+" "+log_message + '\n')  # 以追加的方式写入日志文件

# 统计文件夹及子文件夹下的总文件数
# folder_paths = [r"C:\Users\enjud\SynologyDrive\投稿论文\★档案归档检查自动化\picture2excel"]
# folder_regex_list = [re.compile(r'^\d{4}年彩色$')]
# exclude_extensions = ['.json', '.xlsx'] 均为小写即可
# exclude_folders = ['参考','alitest']
#返回也是列表，给定绝对/相对路径，就返回绝对/相对路径
def filtered_files(folder_paths, exclude_folders=[], exclude_extensions=[], exclude_files=[], folder_regex_list=[]):
    total_files = 0
    files_names = []
    files_paths = []

    for folder_path in folder_paths:
        for root, dirs, files in os.walk(folder_path):
            # 排除指定文件夾名稱，排除json和table文件
            for folder in exclude_folders:
                if folder in dirs:
                    dirs.remove(folder)
                    
            # 檢查folder_regex_list是否為空，不為空則按照正則表達式列表過濾文件夾
            if folder_regex_list:
                dirs[:] = [d for d in dirs if not any(regex.match(d) for regex in folder_regex_list)]
    
            for file in files:
                # 排除指定文件擴展名
                # if any(file.endswith(ext) for ext in exclude_extensions):
                #     continue
                # 将文件扩展名转换为小写
                file_ext = os.path.splitext(file)[1].lower()
                # 排除指定文件擴展名，排除pdf和txt文件 (忽略大小写)
                if any(file_ext == ext.lower() for ext in exclude_extensions):
                    continue
                # 排除指定文件名
                if file in exclude_files:
                    continue
                total_files += 1
                files_names.append(file)
                files_paths.append(os.path.join(root, file))

    return total_files, files_names, files_paths

# 检查指定文件是否存在
def check_file_existence(file_path:str)->bool:
    if os.path.exists(file_path):
        printLog(f"The file {file_path} exists.")
        return True
    else:
        printLog(f"The file {file_path} does not exist.")
        return False

# 在data_value里面进行正则查找，存入df，并添加file_path列   
def regular_find_to_df(data_value, file_path, columns, pattern,split_num):
    matches = re.finditer(pattern, json.dumps(data_value, ensure_ascii=False))

    serial_numbers_positions = []

    for match in matches:
        serial_numbers_positions.append((match.group(0), match.start()))

    serial_numbers_positions = serial_numbers_positions[23:]

    df = process_serial_numbers(serial_numbers_positions, split_path(os.path.abspath(file_path), '电子档案'),split_num)
    df.columns = columns

    return df

# 将df数据类型写入文件
def generate_table_excel(data_value, file_path, columns, pattern,xlspath,split_num):
    df = regular_find_to_df(data_value, file_path, columns, pattern,split_num)
    df.to_excel(xlspath, index=False)
    printLog("Excel table generated successfully.")

# 对给定路径从给定文件夹名称处进行截取，变成相对路径
def split_path(path, folder_name):
    """
    将绝对路径转换为相对路径，不包含给定的文件夹名称
    :param path: 绝对路径
    :param folder_name: 文件夹名称作为参考路径
    :return: 相对路径
    """
    # 将绝对路径分割成部分
    parts = path.split(os.sep)
    
    # 找到folder_name的位置
    try:
        index = parts.index(folder_name)
    except ValueError:
        # 如果folder_name不在路径中，返回原始绝对路径
        return path
    
    # 从folder_name的下一个位置开始截取路径，避免包含folder_name
    relative_path_parts = parts[index + 1:]
    
    # 构建完整的相对路径，包括文件名
    full_relative_path = os.sep.join(relative_path_parts)
    
    return full_relative_path

# 从json文件中的prism_tables_info列表中提取单元格坐标和行数信息，存入excel表
def jsonAxes_to_excel(excel_file_name, org_image_path,prism_tables_info,columns_num):
    rectangles = []
    tableCellIds = []
    num = []

    count = 0
    st_ysc = -1
    st_num = -1
    temp_points = []

    for table_info in prism_tables_info:
        for cell_info in table_info.get('cellInfos', []):
            if count >= columns_num+1:
                pos = cell_info.get('pos', {})

                for point in pos:
                    x = point['x']
                    y = point['y']

                    temp_points.append((x, y))
                rectangles.append(temp_points)
                
                tableCellId = int(cell_info.get('tableCellId', 0))
                tableCellIds.append(tableCellId)

                ysc = cell_info.get('ysc', 0)
                word = cell_info.get('word', 0)

                if ysc > st_ysc:
                    st_ysc = ysc
                    st_num = word
                num.append(st_num)

                temp_points = []
            count += 1

    data = {
        'num': num,
        'tableCellId': tableCellIds,
        'axes': rectangles
    }

    df = pd.DataFrame(data)

    df.insert(loc=0, column='orgImage_path', value=org_image_path)

    columns = ['orgImage_path', 'num', 'tableCellId', 'axes']
    df = df.reindex(columns=columns)

    df.to_excel(excel_file_name, index=False)
    return 1

# 返回表格标题行数量，tableCellID和word的元组列表，标题行tableCellID的数量
# json_data=eval(json_data["body"]["Data"])
# prism_tables_info = json_data["prism_tablesInfo"]
def tableTitleRowNum(json_data):
    json_data1=eval(json_data["body"]["Data"])
    prism_tables_info = json_data1["prism_tablesInfo"]
    titleRowNum=0
    titleRow=[]
    for table_info in prism_tables_info:
        xCellSize=table_info['xCellSize']
        yCellSize=table_info['yCellSize']
        tableTitleLen=xCellSize
        for cell_info in table_info.get('cellInfos', []):
            yec0=cell_info.get('yec', 0)
            ysc0=cell_info.get('ysc', 0)
            xsc0=cell_info.get('xsc', 0)
            if xsc0<tableTitleLen:
                row0=yec0-ysc0+1
                if row0>titleRowNum:
                    titleRowNum=row0
    for table_info in prism_tables_info:
        for cell_info in table_info.get('cellInfos', []):
            ysc0=cell_info.get('ysc', 0)
            word0=cell_info.get('word', 0)
            if ysc0<titleRowNum:
                titleRow.append(word0)
    titleRowLen=len(titleRow)
    dataRowNum=yCellSize-titleRowNum
    return titleRowNum,dataRowNum,titleRowLen #返回标题一共有几行，除去标题行的数据条目数量，标题所有字段粗略数量

def tableTitle(json_data):
    json_data1=eval(json_data["body"]["Data"])
    prism_tables_info = json_data1["prism_tablesInfo"]
    temp=[]
    temp0=[]
    row=[]
    _,dataRowNum,titleRowLen=tableTitleRowNum(json_data)
    for table_info in prism_tables_info:
        for cell_info in table_info.get('cellInfos', [])[:titleRowLen]:
            yec0=cell_info.get('yec', 0)
            ysc0=cell_info.get('ysc', 0)
            xec0=cell_info.get('xec', 0)
            xsc0=cell_info.get('xsc', 0)
            word0=cell_info.get('word', 0)
            xse=xec0-xsc0
            yse=yec0-ysc0
            if ysc0==0:
                row.append(word0)
            if xse>0 and ysc0==0 and yse==0:
                temp.append((xsc0,xse,word0))
            if xse==0 and ysc0==1 and yse==0:
                temp0.append(word0)
    while temp:
        # 删除索引的元素，并获取删除的元素
        pop_element = temp.pop(0)
        extracted_values = temp0[:pop_element[1]+1]
        # 获取值的索引
        index = row.index(pop_element[2])
        row.pop(index)
        # 使用切片将要插入的元素分开
        left_part = row[:index]
        
        right_part = row[index:]

        # 将左侧部分、要插入的值、右侧部分合并起来
        my_list = left_part + extracted_values + right_part

        # 通过循环逐个删除提取的值
        for value in extracted_values:
            temp0.pop(temp0.index(value))

    return my_list,titleRowLen,dataRowNum  # 返回列表形式的标题有效字段名称，标题所有字段粗略数量

def json_to_df(json_data,db_query,filepath,key_table_name="xschemeKeyTable",dfType="list-dict"):
    # 获取 "Data" 字段的值
    json_data1=eval(json_data["body"]["Data"])
    prism_tables_info = json_data1["prism_tablesInfo"]
    tableHeadTail = json_data1["tableHeadTail"]
    tableHead0=tableHeadTail[0]['head'][0]
    tableHead1=tableHeadTail[0]['head'][1]

    
    st_ysc = -1
    st_num = -1
    
    countToll = 0
    temp_points = []
    
    tableCellId=[]
    yec=[]
    ysc=[]
    xec=[]
    xsc=[]
    num=[]
    archiveCode=[]
    word=[]
    axes=[]
    keyCode=[]
    # 编写正则表达式来匹配四位数字作为年份
    year_pattern = r"(\d{4})"
    
    # 使用正则表达式进行匹配
    year = re.search(year_pattern, tableHead0)[0]
    
    province_pattern =r'(?:(北京|天津|上海|重庆)|(河北|山西|内蒙古|辽宁|吉林|黑龙江|江苏|浙江|安徽|福建|江西|山东|河南|湖北|湖南|广东|海南|四川|贵州|云南|陕西|甘肃|青海|台湾)|(广西|西藏|宁夏|新疆)|(香港|澳门))'
    
    # 使用正则表达式进行匹配
    province = re.search(province_pattern, tableHead0)[0]
    
    admission_batch_pattern =r'([本科|专科|研究生|普通类本科批|特殊类型|提前批|第一批|文理本科|文理科本科|国家|高校]+)(普通批|提前批|第一批|一批|二批|高职\(专科\)批|A阶段|招生志愿|艺术B段|第一批B段|提前B|专项)'
    # 使用正则表达式进行匹配
    admissionBatch = re.search(admission_batch_pattern, tableHead1)[0]

    archive_code_pattern=r'\d{4}-[A-Za-z0-9]{2}\d{2}\.[A-Za-z0-9]{2}-\d+' # 匹配1950-JX11.44-10形式的字符
    archiveCode = re.search(archive_code_pattern, filepath)[0]
    
    titleList,titleRowLen,dataRowNum=tableTitle(json_data)
    for table_info in prism_tables_info:
        xCellSize=table_info['xCellSize']
        yCellSize=table_info['yCellSize']
        for cell_info in table_info.get('cellInfos', []):
            if countToll >= titleRowLen:

                pos = cell_info.get('pos', [])
                for point in pos:
                    x = point['x']
                    y = point['y']
                    temp_points.append((x, y))
                axes.append(temp_points)
                temp_points=[]
        
                tableCellId.append(int(cell_info.get('tableCellId', 0)))
                word0=cell_info.get('word', 0)
                word.append(word0)
                yec0=cell_info.get('yec', 0)
                yec.append(yec0)
                ysc0=cell_info.get('ysc', 0)
                ysc.append(ysc0)
                xec0=cell_info.get('xec', 0)
                xec.append(xec0)
                xsc0=cell_info.get('xsc', 0)
                xsc.append(xsc0)

                if ysc0 > st_ysc:
                    st_ysc = ysc0
                    st_num = word0
                num.append(st_num)

                keyname_to_query = titleList[xsc0]
                # 构建查询条件
                condition =f"FIND_IN_SET('{keyname_to_query}', REPLACE(orgName, '|', ',')) > 0"

                query_result = db_query.query_data(key_table_name, select_fields='keyCode', condition=condition)
                default_value = "NA"

                if query_result:
                    keyCode.append(query_result[0][0])
                else:
                    keyCode.append(default_value)

            countToll += 1

    data = {
        'yec':yec,
        'ysc':ysc,
        'xec':xec,
        'xsc':xsc,
        'word':word,
        'num': num,
        'tableCellId': tableCellId,
        'axes':axes,

        'archiveCode':archiveCode,
        'keyCode':keyCode,
        'year':year,
        'province':province,
        'admissionBatch':admissionBatch
    }

    df = pd.DataFrame(data)
    
    df.insert(loc=0, column='filepath', value=filepath)
    df['xCellSize'] = xCellSize
    df['yCellSize'] = yCellSize
    
    commonDict={"filePath":filepath,"archiveCode":archiveCode,"year":year,"province":province,"admissionBatch":admissionBatch}

    if dfType=="list-dict":
        data_list = df.to_dict(orient='records')
        result=data_list
    elif dfType=="df":
        result=df
    cellNum=xCellSize*dataRowNum
    return result,commonDict,titleRowLen,dataRowNum,cellNum # 返回df形式的每个table的cell相关信息，字典形式的所有单元格字段值都相同的字段，标题行粗略长度，数据条目长度，单元格数量

# 将df存入数据库，数据表名错误，字段值为“NA”或条目不存在，都会导致函数执行无错误信息，可以检查数据表名，把字段值设为空"",这样可以正常插入
def df_db(table_name,cell_name,db_query,json_data,filepath,logName='image2tableProcessLog'):
    result,commonDict,titleRowLen,dataRowNum,cellNum=json_to_df(json_data,db_query,filepath=filepath,dfType='df')
    
    select_fields=f"COUNT(*)"
    condition=f"filePath='{filepath}'"
    checkTable=db_query.query_data(table_name, select_fields, condition=condition)[0][0]

    resultLen=len(result) 
    if(db_query.insert_row(cell_name,result.to_dict(orient='records'))):
        if resultLen==cellNum:
            printLog(f"'{filepath}' OCR识别完整，json已录入cell数据库;")
            value={'cell':1}
            db_query.update_row(logName, value, condition)
        elif 0<resultLen<cellNum:
            value=" \\\\n "+str(datetime.datetime.now())+" OCR识别单元格Cell不完整，json已录入Cell;"
            printLog(value)
            db_query.append_value(logName,"errorInfo", value, condition)
            value={'cell':2}
            db_query.update_row(logName, value, condition)
        else:
            value=" \\\\n "+str(datetime.datetime.now())+" OCR识别单元格Cell失败或超出可能数量，将删除已导入Cell单元格数据;"
            db_query.delete_row(cell_name,condition)
            printLog(value)
            db_query.append_value(logName,"errorInfo", value, condition)

    if checkTable==dataRowNum:
        value=" \\\\n "+str(datetime.datetime.now())+" json已录入table数据库;"
        db_query.append_value(logName,"errorInfo", value, condition)
        value={'table':1}
        db_query.update_row(logName, value, condition)
    elif 0<checkTable<dataRowNum:
        value=" \\\\n "+str(datetime.datetime.now())+" json录入table数据时发生问题，将删除录入不完整的数据;"
        db_query.append_value(logName,"errorInfo", value, condition)
        db_query.delete_row(table_name,condition)
        value={'tab':0}
        db_query.update_row(logName, value, condition)
    else:
        # 将数据转换为列表
        word_list = result['word'].tolist()
        ysc_list=result['ysc'].tolist()
        # 每x行为一组，创建新的DataFrame
        x = titleRowLen-1
        new_data = []
        current_num = None
        row_data = []
        
        for word, ysc in zip(word_list, ysc_list):
            if ysc != current_num:
                if current_num is not None:
                    row_data += ['NA'] * (x - len(row_data))
                    new_data.append(row_data)
        
                current_num = ysc
                row_data = []
        
            row_data.append(word)
        
        # 处理最后一行数据
        row_data += ['NA'] * (x - len(row_data))
        new_data.append(row_data)
        keycode_list = result['keyCode'].unique()
        df_dict = pd.DataFrame(new_data, columns=keycode_list).to_dict(orient='records')
    
        # 遍历每个字典元素并添加多个元素
        for d in df_dict:
            d.update(commonDict)
            if(db_query.insert_row(table_name,df_dict)):
                value={'tab':1}
                db_query.update_row(logName, value, condition)

# 从cell信息表中获取坐标，在图像上对给定行以外的行填充，输出原图质量的图像
def format_image_from_excel(orgImage_path,excel_file,row_number):

    # 从 Excel 文件中读取数据到 DataFrame
    df = pd.read_excel(excel_file)

    # 检查某个字段值是否包含给定变量
    if df['num'].isin([row_number]).any():

        # 打开图像
        image = Image.open(orgImage_path)

        # 获取原始图像的分辨率
        dpi = image.info.get('dpi')
        # 在原始图像上进行填充操作
        draw = ImageDraw.Draw(image)
        rectangle_points_list = []
        # 循环遍历 DataFrame，对符合条件的单元格进行操作
        for index, row in df.iterrows():
            if row['num'] != row_number:
                # 对其他单元格进行白色填充
                rectangle_points_list.append(row['axes'])

        # 循环遍历所有矩形坐标列表并填充
        for rectangle_points in rectangle_points_list:
            draw.polygon(eval(rectangle_points), outline='black', fill='white')

        # 保存填充后的图像到文件
        output_path = r"./0001test.jpg"
        image.save(output_path, 'JPEG', dpi=dpi)
        printLog("图片已保存。")

    else:
        printLog("数据不存在.")

# 从cell信息表中获取坐标，在图像上对给定行以外的行填充，输出原图质量的图像
def format_image_from_db(table,orgImage_path,db_query,row_number,output_path=''):
    # 构造查询条件
    condition = f"{'filePath'} = '{orgImage_path}' AND {'num'} != '{row_number}'"
    
    result = db_query.query_data(table, 'axes', condition)
    if result:
        result=[row[0] for row in result]  # 返回字段3的值列表

    else:
        return []
    # 打开图像
    image = Image.open(orgImage_path)
    # 获取原始图像的分辨率
    dpi = image.info.get('dpi')
    # 在原始图像上进行填充操作
    draw = ImageDraw.Draw(image)
    for rectangle_points in result:
        draw.polygon(eval(rectangle_points), outline='black', fill='white')

    # 保存填充后的图像到文件
    if output_path:
        image.save(output_path, 'JPEG', dpi=dpi)
    return image

# 检查图像两个方向是否超过阈值，阿里云要求不能超过8192px    
def check_image_resolution(img, max_width, max_height):
    """
    检查图像在横向和纵向两个方向的分辨率是否超过指定的阈值
    :param image_path: 图像文件路径
    :param max_width: 最大宽度阈值
    :param max_height: 最大高度阈值
    :return: True（未超过阈值）或 False（超过阈值）
    """
    try:
        # 获取图像的宽度和高度
        width, height = img.size
        
        # 检查分辨率是否超过阈值
        if width <= max_width and height <= max_height:
            return True
        else:
            return False
    except Exception as e:
        # 处理异常情况
        printLog("Error:", e)
        return None

# 将PIL对象按照max_size进行等比缩小，并返回缩小后的PIL对象    
def resize_image_resolution(img, max_size):
    """
    按比例缩小图像，确保长宽的最大值不超过指定的数值
    :param img: Pillow 打开后的图像对象
    :param max_size: 缩小后的长宽最大值
    :return: 缩小后的 Pillow 图像对象
    """
    try:
        # 计算缩小比例
        width, height = img.size
        max_dimension = max(width, height)
        scale_factor = max_dimension / max_size
        
        # 计算缩小后的长宽
        new_width = int(width / scale_factor)
        new_height = int(height / scale_factor)
        
        # 缩小图像（等比缩放）
        img.thumbnail((new_width, new_height))
        
        printLog("图像已成功按比例缩小，长宽的最大值不超过指定数值")
        return img
    except Exception as e:
        # 处理异常情况
        printLog("Error:", e)
        return None