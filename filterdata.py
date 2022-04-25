import json
from sqlalchemy import func
from flask import jsonify,Response
from config import app
from model import db, demograpic_data
from sqlalchemy.sql import label
from create_task import Create_Chart,Create_School_Chart
import os


@app.route('/categorywisegender/', methods=['GET'])
def categorywise_gender():
  
   query = db.session.query(label('category',demograpic_data.category), 
                            label("female",func.sum(demograpic_data.female)), 
                            label("male",func.sum(demograpic_data.male))).group_by(demograpic_data.category).all()
   data = [r._asdict() for r in query]
   result = Create_Chart.apply_async(args=[data, 'CategoeryWise_Gender_Data', 'Category'])
   
   full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
   response = {}
   response["Image_Path"] = full_filename
   return Response(json.dumps(response), mimetype='text/json')

@app.route('/categorywiserace/', methods = ['GET'])
def categorywise_race():
   
    query =  db.session.query(label("category",demograpic_data.category),
                              label(r"#asian",func.sum(demograpic_data.asian)),
                              label(r"%asian",func.sum(demograpic_data.per_asian)),
                              label(r"black",func.sum(demograpic_data.black)),
                              label(r"%black",func.sum(demograpic_data.per_black)),
                              label(r"hispanic",func.sum(demograpic_data.hispanic)),
                              label(r"%hispanic",func.sum(demograpic_data.per_hispanic)),
                              label(r"other",func.sum(demograpic_data.other)),
                              label(r"%other",func.sum(demograpic_data.per_other)),
                              label(r"white",func.sum(demograpic_data.white)),
                              label(r"%white",func.sum(demograpic_data.per_white))).group_by(demograpic_data.category).all()
    data = [r._asdict() for r in query]
    result = Create_Chart.apply_async(args=[data, 'CategoeryWise_Race_Data', 'Category'])
  
    full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
    response = {}
    response["Image_Path"] = full_filename
    return Response(json.dumps(response), mimetype='text/json')


@app.route('/categorywise_grade/', methods = ['GET'])
def categorywise_grade():
    query =  db.session.query(label('category',demograpic_data.category),
                              label("GradeK",func.sum(demograpic_data.GradeK)),
                              label("Grade1",func.sum(demograpic_data.grade1)),
                              label("Grade2",func.sum(demograpic_data.grade2)),
                              label("Grade3",func.sum(demograpic_data.grade3)),
                              label("Grade4",func.sum(demograpic_data.grade4)),
                              label("Grade5",func.sum(demograpic_data.grade5)),
                              label("Grade6",func.sum(demograpic_data.grade6)),
                              label("Grade7",func.sum(demograpic_data.grade7)),
                              label("Grade8",func.sum(demograpic_data.grade8))).group_by(demograpic_data.category).all()
    data = [r._asdict() for r in query]
    result = Create_Chart.apply_async(args=[data, 'CategoeryWise_Grade_Data', 'Category'])
    full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
    response = {}
    response["Image_Path"] = full_filename
    return Response(json.dumps(response), mimetype='text/json') 
  
@app.route('/categorywise_language/', methods = ['GET'])
def categorywise_language():
   
    query =  db.session.query(label('category',demograpic_data.category),
                              label(r"#ELL_Spanish",func.sum(demograpic_data.ell_spanish)),
                              label(r"%ELL_Spanish",func.sum(demograpic_data.per_ell_spanish)),
                              label(r"#ELL_Chinese",func.sum(demograpic_data.ell_chinese)),
                              label(r"%ELL_Chinese",func.sum(demograpic_data.per_ell_chinese)),
                              label(r"#ELL_Bengali",func.sum(demograpic_data.ell_bengali)),
                              label(r"%ELL_Bengali",func.sum(demograpic_data.per_ell_bengali)),
                              label(r"#ELL_Arabic",func.sum(demograpic_data.ell_arabic)),
                              label(r"%ELL_Arabic",func.sum(demograpic_data.per_ell_arabic)),
                              label(r"#ELL_Haitian_Creole",func.sum(demograpic_data.ell_haitian_creole)),
                              label(r"%ELL_Haitian_Creole",func.sum(demograpic_data.per_ell_haitian_creole)),
                              label(r"#ELL_French",func.sum(demograpic_data.ell_french)),
                              label(r"%ELL_French",func.sum(demograpic_data.per_ell_french)),
                              label(r"#ELL_Russian",func.sum(demograpic_data.ell_russian)),
                              label(r"%ELL_Russian",func.sum(demograpic_data.per_ell_russian)),
                              label(r"#ELL_Korean",func.sum(demograpic_data.ell_korean)),
                              label(r"%ELL_Korean",func.sum(demograpic_data.per_ell_korean)),
                              label(r"#ELL_Urdu",func.sum(demograpic_data.ell_urdu)),
                              label(r"%ELL_Urdu",func.sum(demograpic_data.per_ell_urdu)),
                              label(r"#ELL_Other",func.sum(demograpic_data.ell_other)),
                              label(r"%ELL_Other",func.sum(demograpic_data.per_ell_other))).group_by(demograpic_data.category).all()
    data = [r._asdict() for r in query]
    result = Create_Chart.apply_async(args=[data, 'CategoeryWise_Language_Data', 'Category'])
  
    full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
    response = {}
    response["Image_Path"] = full_filename
    return Response(json.dumps(response), mimetype='text/json')

@app.route('/categorywise_level/', methods = ['GET'])
def categorywise_level():
    query = db.session.query(label("category",demograpic_data.category),
                             label(r"#ELA_Level1",func.sum(demograpic_data.ela_level1)),
                             label(r"%ELA_Level1",func.sum(demograpic_data.ela_per_level1)),
                             label(r"#ELA_Level2",func.sum(demograpic_data.ela_level2)),
                             label(r"%ELA_Level2",func.sum(demograpic_data.ela_per_level2)),
                             label(r"#ELA_Level3",func.sum(demograpic_data.ela_level3)),
                             label(r"%ELA_Level3",func.sum(demograpic_data.ela_per_level3)),
                             label(r"#ELA_Level4",func.sum(demograpic_data.ela_level4)),
                             label(r"%ELA_Level4",func.sum(demograpic_data.ela_per_level4)),
                             label(r"#ELA_L3+L4",func.sum(demograpic_data.ela_l3_l4)),
                             label(r"%ELA_L3+L4",func.sum(demograpic_data.ela_per_l3_l4))).group_by(demograpic_data.category).all()
    data = [r._asdict() for r in query]
    result = Create_Chart.apply_async(args=[data, 'CategoeryWise_ELA_LEVEL_Data', 'Category'])
   
    full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
    response = {}
    response["Image_Path"] = full_filename
    return Response(json.dumps(response), mimetype='text/json')

@app.route('/categorywise_math_level/', methods = ['GET'])
def categorywise_math_level():
    query =  db.session.query(label("category",demograpic_data.category),
                              label(r"MATH #Level1",func.sum(demograpic_data.math_level1)),
                              label(r"MATH %Level1",func.sum(demograpic_data.math_per_level1)),
                              label(r"MATH #Level2",func.sum(demograpic_data.math_level2)),
                              label(r"MATH %Level2",func.sum(demograpic_data.math_per_level2)),
                              label(r"MATH #Level3",func.sum(demograpic_data.math_level3)),
                              label(r"MATH %Level3",func.sum(demograpic_data.math_per_level3)),
                              label(r"MATH #Level4",func.sum(demograpic_data.math_level4)),
                              label(r"MATH %Level4",func.sum(demograpic_data.math_per_level4)),
                              label(r"MATH #L3+L4",func.sum(demograpic_data.math_level_l3)),
                              label(r"MATH %L3+L4",func.sum(demograpic_data.math_per_level_l3_l4))).group_by(demograpic_data.category).all()
    data = [r._asdict() for r in query]
    result = Create_Chart.apply_async(args=[data, 'CategoeryWise_MATH_LEVEL_Data', 'Category'])
    
    full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
    response = {}
    response["Image_Path"] = full_filename
    return Response(json.dumps(response), mimetype='text/json')

@app.route('/schoolwise_schoolenrolll/', methods = ['GET'])
def schoolwise_school_enroll():
    query =  db.session.query(label("SchoolName",demograpic_data.school_name),
                              label(r"TotalEnrollment",func.sum(demograpic_data.totalenrollment))).group_by(demograpic_data.school_name).all()
    data = [r._asdict() for r in query]
    result = Create_School_Chart.apply_async(args=[data, 'SchoolWise_Total_Enroll_Data'])
    
    full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
    response = {}
    response["Image_Path"] = full_filename
    return Response(json.dumps(response), mimetype='text/json')

@app.route('/schoolwise_ela_testtaker/', methods = ['GET'])
def schoolwise_ela_testtaker():
    query =  db.session.query(label('SchoolName',demograpic_data.school_name),
                        label("ELA_TestTaker", func.sum(demograpic_data.ela_test_takers))).group_by(demograpic_data.school_name).all()
    data = [r._asdict() for r in query]
    result = Create_School_Chart.apply_async(args=[data, 'SchoolWise_ELA_TestTaker_Data'])
    
    full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
    response = {}
    response["Image_Path"] = full_filename
    return Response(json.dumps(response), mimetype='text/json')

@app.route('/schoolwise_math_testtaker/', methods = ['GET'])
def schoolwise_math_testtaker():
    query =  db.session.query(label("SchoolName",demograpic_data.school_name),
                              label(r"MATH Test Taker",func.sum(demograpic_data.math_test_taker))).group_by(demograpic_data.school_name).all()
    data = [r._asdict() for r in query]
    result = Create_School_Chart.apply_async(args=[data, 'SchoolWise_Math_TestTaker_Data'])
    
    full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
    response = {}
    response["Image_Path"] = full_filename
    return Response(json.dumps(response), mimetype='text/json')



@app.route('/categorywise_Average_grade/', methods = ['GET'])
def categorywise_Average_grade():
    query =  db.session.query(label('category',demograpic_data.category),
                              label("GradeK",func.round(func.avg(demograpic_data.GradeK))),
                              label("Grade1",func.round(func.avg(demograpic_data.grade1))),
                              label("Grade2",func.round(func.avg(demograpic_data.grade2))),
                              label("Grade3",func.round(func.avg(demograpic_data.grade3))),
                              label("Grade4",func.round(func.avg(demograpic_data.grade4))),
                              label("Grade5",func.round(func.avg(demograpic_data.grade5))),
                              label("Grade6",func.round(func.avg(demograpic_data.grade6))),
                              label("Grade7",func.round(func.avg(demograpic_data.grade7))),
                              label("Grade8",func.round(func.avg(demograpic_data.grade8)))).group_by(demograpic_data.category).all()
    data = [r._asdict() for r in query]
    result = Create_Chart.apply_async(args=[data, 'CategoeryWise_Grade_Data', 'Category'])
    full_filename = os.path.join(os.path.join(app.root_path,app.config['IMAGES_FOLDER']), result.get())
    response = {}
    response["Image_Path"] = full_filename
    return Response(json.dumps(response), mimetype='text/json') 