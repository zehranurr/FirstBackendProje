from flask import Flask,render_template,request,redirect,url_for
import psycopg2
app = Flask(__name__,template_folder='templates',static_folder='static')
conn= psycopg2.connect(
        database="smarket",
        user='postgres',
        password='12345',
        host='localhost',
        port='5432')


@app.route('/')
def index():
    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."Blog" ')
    rows=cur.fetchall() 

    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."urun" ')
    uruns=cur.fetchall() 

    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."urun" WHERE "Urun_is_new"=True ')
    featured_prodects=cur.fetchall() 

    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."Reklam" ')
    reklamside=cur.fetchall()

    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."markalar" ')
    markas=cur.fetchall() 

    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."Slider" ')
    dataslider=cur.fetchall() 
    



    
    



    return render_template('index.html',data=rows,uruns=uruns,featured_prodects=featured_prodects,reklamside=reklamside,markas=markas,dataslider=dataslider)


@app.route('/admin')

def admin():

    return render_template('admin.html')

@app.route('/admin/rapor')
def rapor():

    return render_template('rapor.html')

@app.route('/admin/marka')
def marka():
    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."markalar" ')
    rows=cur.fetchall() 

    return render_template('marka.html',data=rows)






@app.route('/admin/reklam')
def reklam(): 
    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."Reklam" ')
    rows=cur.fetchall() 


    return render_template('reklam.html',data=rows)


@app.route('/register')
def register():

    return render_template('register.html')

@app.route('/admin/Blog')
def blog():
    
    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."Blog" ')
    rows=cur.fetchall() 

    return render_template('Blog.html',data=rows)

@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/base')
def base():
    

    return render_template('base.html')


@app.route('/admin/urun')
def urun():

    

    cur =conn.cursor()
    print(cur)
    cur.execute('SELECT * FROM public."urun" ')
    rows=cur.fetchall() 

    return render_template('urun.html',data=rows)

@app.route('/menu')
def menu():

    return render_template('menu.html')




@app.route('/admin/markaekle',methods=['GET','POST'])
def markaekle():
    if request.method=='GET':
        print("data gelmedi")
    if request.method=='POST':
        marka_imaj=request.form['marka_imaj']    
        marka_order=request.form['order']
        cur=conn.cursor()
        cur.execute('INSERT INTO public."markalar"("marka_imaj","order")''VALUES(%s,%s)',(marka_imaj,marka_order))
        conn.commit()
        
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."markalar" ')
        rows=cur.fetchall() 



        return render_template('marka.html',data=rows)
    return render_template('markaekle.html')
    


@app.route('/admin/urunekle',methods=['GET','POST'])
def urunekle():
    if request.method=='GET':
        print("data gelmedi")
        



    if request.method=='POST':
        urun_ad=request.form['urun_ad']
        urun_fiyat=request.form['urun_fiyat']
        Urun_resim=request.form['Urun_resim']
        urun_info=request.form['Urun_info']

        print(urun_ad)
        print(urun_fiyat)
        print(Urun_resim)
        print(urun_info)

        cur=conn.cursor()
        cur.execute('INSERT INTO public."urun"("Urun_ad","Urun_fiyat","Urun_resim","Urun_info")''VALUES (%s,%s,%s,%s)',(urun_ad,urun_fiyat,Urun_resim,urun_info))
        conn.commit()
        
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."urun" ')
        rows=cur.fetchall() 



        return render_template('urun.html',data=rows)
    
    return render_template('urunekle.html')



@app.route('/admin/reklamekle',methods=['GET','POST'])
def reklamekle():
    if request.method=='GET':
        print("data gelmedi")
        



    if request.method=='POST':
        reklam_resim=request.form['resim']
        reklam_title=request.form['title']
        reklam_aciklama=request.form['Aciklama']


        

    
        cur=conn.cursor()
        cur.execute('INSERT INTO public."Reklam"("resim","title","Aciklama")''VALUES (%s,%s,%s)',(reklam_resim,reklam_title,reklam_aciklama))
        conn.commit()
        
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."Reklam" ')
        rows=cur.fetchall() 



        return render_template('reklam.html',data=rows)
    
    return render_template('reklamekle.html')





@app.route('/admin/urunupdate',methods=['GET', 'POST'])
def urunupdate():
    if request.method=='GET':
        urun_id=request.args.get('id')
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."urun" WHERE "id"=%s;',[urun_id])

        rows=cur.fetchall() 
        return render_template('urunupdate.html',data=rows)

    if request.method=='POST':
        urun_id=request.args.get('id')
        urun_ad=request.form['urun_ad']
        urun_fiyat=request.form['urun_fiyat']
        Urun_resim=request.form['Urun_resim']
        urun_info=request.form['Urun_info']

        print(urun_ad)
        print(urun_fiyat)
        print(Urun_resim)
        print(urun_info)

        cur=conn.cursor()
        cur.execute('UPDATE public."urun"  SET "Urun_ad"=%s,"Urun_fiyat"=%s,"Urun_resim"=%s,"Urun_info"=%s WHERE "id"=%s',(urun_ad,urun_fiyat,Urun_resim,urun_info,urun_id))
        conn.commit()
        
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."urun" ')
        rows=cur.fetchall() 



        return render_template('urun.html',data=rows)
    
    return render_template('urun.html',data=rows)


@app.route('/admin/markagüncelle',methods=['GET', 'POST'])
def markagüncelle():
    if request.method=='GET':
        marka_id=request.args.get('id')
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."markalar" WHERE "id"=%s;',[marka_id])

        rows=cur.fetchall() 
        return render_template('markagüncelle.html',data=rows)
    if request.method=='POST':
        marka_id=request.args.get('id')
        marka_imaj=request.form['marka_imaj']    
        marka_order=request.form['order']
        cur=conn.cursor()
        cur.execute('UPDATE public."markalar"  SET "marka_imaj=%s,"order"=%s WHERE "id"=%s',(marka_imaj,marka_order,marka_id))
        conn.commit()
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."markalar" ')
        rows=cur.fetchall() 



        return render_template('marka.html',data=rows)
    
    return render_template('marka.html',data=rows)
@app.route('/admin/reklamgüncelle',methods=['GET', 'POST'])
def reklamgüncelle():
    if request.method=='GET':
        reklam_id=request.args.get('id')
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."Reklam" WHERE "id"=%s;',[reklam_id])
        rows=cur.fetchall() 
        return render_template('reklamgüncelle.html',data=rows)

    if request.method=='POST':
        reklam_id=request.args.get('id')
        title=request.form['title']    
        Aciklama=request.form['Aciklama']
        resim=request.form['resim']
        cur=conn.cursor()
        cur.execute('UPDATE public."Reklam"  SET "title"=%s,"Aciklama"=%s ,"resim"=%s WHERE "id"=%s',(title,Aciklama,resim,reklam_id))
        conn.commit()
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."Reklam" ')
        data=cur.fetchall() 



        return render_template('reklam.html',data=data)
    
    return render_template('reklam.html',data=data)



@app.route('/admin/bloggüncelle',methods=['GET', 'POST'])
def bloggüncelle():
    if request.method=='GET':
        blog_id=request.args.get('id')
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."Blog" WHERE "id"=%s;',[blog_id])
        rows=cur.fetchall() 

    if request.method=='POST':
        reklam_id=request.args.get('id')
        publishdate=request.form['publish_date']
        title=request.form['title']    
        Aciklama=request.form['Aciklama']
        resim=request.form['resim']
        uzunbaslık=request.form['uzun_baslik']
        yazar=request.form['yazar']
        cur=conn.cursor()
        cur.execute('UPDATE public."Blog"  SET "title=%s,"Aciklama"=%s ,"resim"=%s ,"publish_date"=%s,"uzun_baslik"=%s,"yazar"=%s WHERE "id"=%s',(title,Aciklama,resim,reklam_id,publishdate,uzunbaslık,yazar))
        conn.commit()
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."Blog" ')
        rows=cur.fetchall() 



        return render_template('blog.html',data=rows)
    
    return render_template('blog.html',data=rows)





@app.route('/admin/urunsil',methods=['GET'])
def urunsil():
    if request.method=='GET':
        urun_id=request.args.get('id')
        
        cur=conn.cursor()
        cur.execute('DELETE FROM public."urun" WHERE "id"=%s;',[urun_id])
        conn.commit()
        
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."urun" ')
        rows=cur.fetchall() 



        return render_template('urun.html',data=rows)

    


    return render_template('urun.html')
@app.route('/admin/reklamsil',methods=['GET'])
def reklamsil():
    if request.method=='GET':
        urun_id=request.args.get('id')
        
        cur=conn.cursor()
        cur.execute('DELETE FROM public."Reklam" WHERE "id"=%s;',[urun_id])
        conn.commit()
        
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."Reklam" ')
        rows=cur.fetchall() 



        return render_template('reklam.html',data=rows)

    


    return render_template('reklam.html',data=rows)


@app.route('/admin/markasil',methods=['GET'])
def markasil():
    if request.method=='GET':
        urun_id=request.args.get('id')
        
        cur=conn.cursor()
        cur.execute('DELETE FROM public."markalar" WHERE "id"=%s;',[urun_id])
        conn.commit()
        
        cur =conn.cursor()
        print(cur)
        cur.execute('SELECT * FROM public."markalar" ')
        rows=cur.fetchall() 



        return render_template('marka.html',data=rows)

    


    return render_template('marka.html')


if __name__ == '__main__':
    app.run(debug=True)