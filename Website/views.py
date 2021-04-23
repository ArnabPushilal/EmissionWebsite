from flask import Blueprint ,render_template,request,flash
from flask_login import login_required, current_user
from .models import Upload
from .models import Vehicle
from .models import Test
from . import db
import pandas as pd

views = Blueprint('views', __name__)

ALLOWED_EXTENSIONS = {'xlsx'}
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('remarks')
        if 'file' not in request.files:
            flash('No file part')
        files = request.files.getlist('file')
        for file in files:
         inxcel=pd.read_excel(file, sheet_name='Chassis Dyno Format')
         COcold=inxcel.iloc[41,7]
         COhot=inxcel.iloc[41,8]
         COfinal=inxcel.iloc[41,9]

         HCcold=inxcel.iloc[42,7] 
         HChot=inxcel.iloc[42,8] 
         HCfinal=inxcel.iloc[43,9]

         NMHCcold=inxcel.iloc[43,7]
         NMHChot=inxcel.iloc[43,8]
         NMHCfinal=inxcel.iloc[43,9]

         NOXcold=inxcel.iloc[44,7]
         NOXhot=inxcel.iloc[44,8]
         NOxfinal=inxcel.iloc[44,9]

         CO2cold=inxcel.iloc[47,7]
         CO2hot=inxcel.iloc[47,8]
         CO2final=inxcel.iloc[47,9]

         FEcold=inxcel.iloc[49,7]
         FEhot=inxcel.iloc[49,8]
         FEfinal=inxcel.iloc[49,9]

         frmno=inxcel.iloc[9,5]
         engno=inxcel.iloc[10,5]
         test_id=inxcel.iloc[3,6]
         model_name=inxcel.iloc[4,6]
         Rider=inxcel.iloc[5,12]
         DBT=inxcel.iloc[17,9]
         RH=inxcel.iloc[18,9]
         CORRFAC=inxcel.iloc[20,9]
         if len(note) < 1:
           flash('Remarks is too short!', category='error')
         else:
           new_value = Upload(Rider=Rider,test_id=test_id,remarks=note, user_id=current_user.id,COfinal=COfinal,COhot=COhot,COcold=COcold,HCcold=HCcold,HChot=HChot,HCfinal=HCfinal,NMHCcold=NMHCcold,NMHChot=NMHChot,NMHCfinal=NMHCfinal,NOxcold=NOXcold,NOxhot=NOXhot,NOxfinal=NOxfinal,CO2cold=CO2cold,CO2hot=CO2hot,CO2final=CO2final,FEcold=FEcold,FEhot=FEhot,FEfinal=FEfinal)
           db.session.add(new_value)
           newvehicle= Vehicle(engno=engno,frmno=frmno,test_id=test_id,model_name=model_name)


           db.session.add(newvehicle)
           db.session.flush()
           test=Test(test_id=test_id,date=new_value.date,vehicle_id=newvehicle.id,RH=RH,NOXFAC=CORRFAC,DBT=DBT)
           db.session.add(test)
           db.session.commit()
           flash('Test Added!', category='success')

    return render_template("home.html", user=current_user)





