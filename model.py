from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,null,DECIMAL
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()




class demograpic_data(db.Model):
    _tablename_ = 'demograpic_data'
    id = Column(Integer, primary_key = True, nullable = False)
    dbn = Column(String)
    school_name = Column(String)
    category = Column(String)
    year = Column(String)
    totalenrollment = Column(Integer, default=null)
    GradeK = Column(Integer, default=null)
    grade1 = Column(Integer, default=null)
    grade2 = Column(Integer, default=null)
    grade3 = Column(Integer, default=null)
    grade4 = Column(Integer, default=null)
    grade5 = Column(Integer, default=null)
    grade6 = Column(Integer, default=null)
    grade7 = Column(Integer, default=null)
    grade8 = Column(Integer, default=null)
    female = Column(Integer, default=null)
    per_female = Column(DECIMAL, default=null)
    male = Column(Integer, default=null)
    per_male = Column(DECIMAL, default=null)
    asian = Column(Integer, default=null)
    per_asian = Column(DECIMAL, default=null)
    black = Column(Integer, default=null)
    per_black = Column(DECIMAL, default=null)
    hispanic = Column(Integer, default=null)
    per_hispanic = Column(DECIMAL, default=null)
    other = Column(Integer, default=null)
    per_other = Column(DECIMAL, default=null)
    white = Column(Integer, default=null)
    per_white = Column(DECIMAL, default=null)
    ell_spanish = Column(Integer, default=null)
    per_ell_spanish = Column(DECIMAL, default=null)
    ell_chinese = Column(Integer, default=null)
    per_ell_chinese = Column(DECIMAL, default=null)
    ell_bengali = Column(Integer, default=null)
    per_ell_bengali = Column(DECIMAL, default=null)
    ell_arabic  = Column(Integer, default=null)
    per_ell_arabic = Column(DECIMAL, default=null)
    ell_haitian_creole = Column(Integer, default=null)
    per_ell_haitian_creole = Column(DECIMAL, default=null)
    ell_french = Column(Integer, default=null)
    per_ell_french = Column(DECIMAL, default=null)
    ell_russian = Column(Integer, default=null)
    per_ell_russian = Column(DECIMAL, default=null)
    ell_korean = Column(Integer, default=null)
    per_ell_korean = Column(DECIMAL, default=null)
    ell_urdu = Column(Integer, default=null)
    per_ell_urdu = Column(DECIMAL, default=null)
    ell_other = Column(Integer, default=null)
    per_ell_other = Column(DECIMAL, default=null)
    ela_test_takers = Column(Integer, default=null)
    ela_level1 = Column(Integer, default=null)
    ela_per_level1 = Column(DECIMAL, default=null)
    ela_level2 = Column(Integer, default=null)
    ela_per_level2 = Column(DECIMAL, default=null)
    ela_level3 = Column(Integer, default=null)
    ela_per_level3 = Column(DECIMAL, default=null)
    ela_level4 = Column(Integer, default=null)
    ela_per_level4 = Column(DECIMAL, default=null)
    ela_l3_l4 = Column(Integer, default=null)
    ela_per_l3_l4 = Column(DECIMAL, default=null)
    math_test_taker = Column(Integer, default=null)
    math_level1 = Column(Integer, default=null)
    math_per_level1 = Column(DECIMAL, default=null)
    math_level2 = Column(Integer, default=null)
    math_per_level2 = Column(DECIMAL, default=null)
    math_level3 = Column(Integer, default=null)
    math_per_level3 = Column(DECIMAL, default=null)
    math_level4 = Column(Integer, default=null)
    math_per_level4 = Column(DECIMAL, default=null)
    math_level_l3 = Column(Integer, default=null)
    math_per_level_l3_l4 = Column(DECIMAL, default=null)
    

    def __init__(self,dbn,school_name,category,year,totalenrollment,GradeK,grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8,female,per_female,male,per_male,asian,per_asian,black,per_black,hispanic,per_hispanic,other,per_other,white,per_white,ell_spanish,per_ell_spanish,ell_chinese,per_ell_chinese,ell_bengali,per_ell_bengali,ell_arabic,per_ell_arabic,ell_haitian_creole,per_ell_haitian_creole,ell_french,per_ell_french,ell_russian,per_ell_russian,ell_korean,per_ell_korean,ell_urdu,per_ell_urdu,ell_other,per_ell_other,ela_test_takers,ela_level1,ela_per_level1,ela_level2,ela_per_level2,ela_level3,ela_per_level3,ela_level4,ela_per_level4,ela_l3_l4,ela_per_l3_l4,math_test_taker,math_level1,math_per_level1,math_level2,math_per_level2,math_level3,math_per_level3,math_level4,math_per_level4,math_level_l3,math_per_level_l3_l4):
        self.dbn = dbn
        self.school_name = school_name
        self.category = category
        self.year = year
        self.totalenrollment = totalenrollment
        self.GradeK = GradeK
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.grade4 = grade4
        self.grade5 = grade5
        self.grade6 = grade6
        self.grade7 = grade7
        self.grade8 = grade8
        self.female = female
        self.per_female = per_female
        self.male = male
        self.per_male = per_male
        self.asian = asian
        self.per_asian = per_asian
        self.black = black
        self.per_black = per_black
        self.hispanic = hispanic
        self.per_hispanic = per_hispanic
        self.other = other
        self.per_other = per_other
        self.white = white
        self.per_white = per_white
        self.ell_spanish = ell_spanish
        self.per_ell_spanish = per_ell_spanish
        self.ell_chinese = ell_chinese
        self.per_ell_chinese = per_ell_chinese
        self.ell_bengali = ell_bengali
        self.per_ell_bengali = per_ell_bengali
        self.ell_arabic  = ell_arabic
        self.per_ell_arabic = per_ell_arabic
        self.ell_haitian_creole = ell_haitian_creole
        self.per_ell_haitian_creole = per_ell_haitian_creole
        self.ell_french = ell_french
        self.per_ell_french = per_ell_french
        self.ell_russian = ell_russian
        self.per_ell_russian = per_ell_russian
        self.ell_korean = ell_korean
        self.per_ell_korean = per_ell_korean
        self.ell_urdu = ell_urdu
        self.per_ell_urdu = per_ell_urdu
        self.ell_other = ell_other
        self.per_ell_other = per_ell_other
        self.ela_test_takers = ela_test_takers
        self.ela_level1 = ela_level1
        self.ela_per_level1 = ela_per_level1
        self.ela_level2 = ela_level2
        self.ela_per_level2 = ela_per_level2
        self.ela_level3 = ela_level3
        self.ela_per_level3 = ela_per_level3
        self.ela_level4 = ela_level4
        self.ela_per_level4 = ela_per_level4
        self.ela_l3_l4 = ela_l3_l4
        self.ela_per_l3_l4 = ela_per_l3_l4
        self.math_test_taker = math_test_taker
        self.math_level1 = math_level1
        self.math_per_level1 = math_per_level1
        self.math_level2 = math_level2
        self.math_per_level2 = math_per_level2
        self.math_level3 = math_level3
        self.math_per_level3 = math_per_level3
        self.math_level4 = math_level4
        self.math_per_level4 = math_per_level4
        self.math_level_l3 = math_level_l3
        self.math_per_level_l3_l4 = math_per_level_l3_l4
        
        
        
    
 