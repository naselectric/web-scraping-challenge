# import necessary libraries
from flask import Flask, render_template,redirect
import pymongo
import mission_to_mars2


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


db = client.marsdb

data=db.datacoll
data2=db.datacoll2
data3=db.datacoll3
data4=db.datacoll4




initial1={'initial':['Hello and welcome to Mars News']}   
data.insert_one(initial1)
initial2={'initial2':['The Green Planet']}
data2.insert_one(initial2)
initial3={'initial3':['']}
data3.insert_one(initial3)

initial4={'initial4':['']}
data4.insert_one(initial4)


# titlelist=mission_to_mars2.titles()
# data.insert_one(titlelist)


# create instance of Flask app
app = Flask(__name__)


@app.route("/")
def index():
    
    query1=data.find()
    x=query1
    for i in x:
        i

    y=i.values()

    for j in y:
        j


    query2=data2.find()
    x1=query2
    for k in x1:
        k

    y2=k.values()


    for l in y2:
        l



    query3=data3.find()
    x2=query3
    for m in x2:
        m

    y3=m.values()


    for n in y3:
        n

    
    
    query4=data4.find()
    x3=query4
    for o in x3:
        o

    y4=o.values()


    for p in y4:
        p
    


    return render_template("index.html",list0=n,list=j,list1=l,list2=p)





@app.route("/scrape")
def scrape():
        titlelist=mission_to_mars2.titles()
        myquery=initial1
        newvalues={'$set':titlelist}
        data.update_one(myquery, newvalues)
        newslist=mission_to_mars2.news()
        myquery2=initial2
        newvalues2={'$set':newslist}
        data2.update_one(myquery2, newvalues2)
        datelist=mission_to_mars2.dates()
        myquery3=initial3
        newvalues3={'$set':datelist}
        data3.update_one(myquery3, newvalues3)

        imageone=mission_to_mars2.first_image()
        myquery4=initial4
        newvalues4={'$set':imageone}
        data4.update_one(myquery4,newvalues4)
       
       
        

        return redirect("/")    




if __name__ == "__main__":
    app.run(debug=True)



    
  