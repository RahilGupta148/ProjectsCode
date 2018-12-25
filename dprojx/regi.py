{% extends "base.html" %}
{% load staticfiles %}
{% block body_block %}
<div class="container">
<div class="jumbotron">

    {% if registered %}
    <h2>Thank you for registering!</h2>
    {% else %}
    <h2>Register Here!</h2>
    <!-- <h3>Just fill out the form.</h3> -->

<div class="row ">
<div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3 col-xs-10 col-xs-offset-1">
<div class="panel-body">
  <form enctype="multipart/form-data" method="POST">
          {% csrf_token %}
          {{ user_form.as_p }}
          {{ profile_form.as_p }}
     <br/>

   <!-- <div class="form-group input-group">
          <span class="input-group-addon"><i class="fa fa-tag"  ></i></span>
          <input type="text" name="user_form.username" placeholder="Username" style="width:100%">   </div>
  <div class="form-group input-group">
           <span class="input-group-addon"><i class="fa fa-lock"  ></i></span>
           <input type="text" name="user_form.password" placeholder="Password" style="width:100%">   </div>

 <div class="form-group input-group">
            <span class="input-group-addon"><i class="fa fa-tag"  ></i></span>
            <input type="text" name="user_form.email" placeholder="Email" style="width:100%">   </div>

  <div class="form-group input-group">
             <span class="input-group-addon"><i class="fa fa-tag"  ></i></span>
             <input type="text" name="user_form.contact" placeholder="Portfolio Site" style="width:100%">   </div> -->
<input type="submit" name="" value="Register">
             <!-- <button type="submit" name="" value="Register" style="background-color:#4CAF50; color: white;
                 padding: 14px 20px;
                 margin: 8px 0;
                 border: none;
                 cursor: pointer;
                 width: 100%;"> Register</button> -->
</form>
    {% endif %}
</div>
</div>
{% endblock %}
