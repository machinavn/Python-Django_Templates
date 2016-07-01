DJANGO View - Model - Template 
View: Chứa những hàm truy cập đến Models ( Models chính là đối tượng )
A view is a place where we put the "logic" of our application. 
It will request information from the model you created before and pass it to a template. 


What is a QuerySet?

A QuerySet is, in essence, a list of objects of a given Model. 
QuerySet allows you to read the data from the database, filter it and order it.


Dynamic data in templates
Dữ liệu động trong template : 
We have different pieces in place: the Post model is defined in models.py, Đối tượng Post trong model.py
we have post_list in views.py and the template added. Post_lít là danh sách các post, là view
But how will we actually make our posts appear in our HTML template? Because that is what we want to do. 
Take some content (models saved in the database) and display it nicely in our template, right?

Queryset là tập hợp các đối tượn g trong models 
