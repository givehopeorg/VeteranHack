function facilities(data){
  console.log(data);
  data = data["facilities"];

  for (var i =0 ; i < data.length; i++){
    ele = data[i];
    d = document.createElement("tr");

    a = document.createElement("a");
    a.href = ele["url"];
    a.innerHTML = ele["url"];
    
    title = document.createElement("span");
    title.innerHTML=ele["name"].replace(/<\/?[^>]+(>|$)/g, " ");

    address = document.createElement("p");
    address.innerHTML= String(ele["address"] + " "+ ele["city"] + ", "  + ele["state"]).replace(/<\/?[^>]+(>|$)/g, "");

    type = document.createElement("p");
    type.innerHTML=ele["type"].replace(/<\/?[^>]+(>|$)/g, " ");

    description = document.createElement("p")
    description.innerHTML=ele["description"].replace(/<\/?[^>]+(>|$)/g, " ");;//replace(/<\/?[^>]+(>|$)/g, " ");


    td = document.createElement("td");
    $(title).appendTo(td);
    $(td).appendTo(d);

    td = document.createElement("td");
    $(description).appendTo(td);    
    $(td).appendTo(d);
    
    td = document.createElement("td");
    $(address).appendTo(td);
    $(td).appendTo(d);
    
    td = document.createElement("td");
    $(type).appendTo(td);
    $(td).appendTo(d);
    
    td = document.createElement("td");
    $(a).appendTo(td);
    $(td).appendTo(d);

    console.log(d);
    $(d).addClass("ele").appendTo("#data_table");

  }

}
function getVData(url,parser){
  var stuff, data, success;
   $.ajax({
    dataType: "json",
    url: url,
    data: data,
    success: function(data){
     // console.log(data);
      parser(data);
      
      //stuff = data;
    }
  });
}

function care (data){
  for (var i =0 ; i < data.length; i++){
    ele = data[i];
    d = document.createElement("tr");

    td2 = document.createElement("td");
    title = document.createElement("span");
    title.innerHTML = data[i]["title"];
    $(title).appendTo(td2);
    $(td2).appendTo(d);

    td3 = document.createElement("td");
    content = document.createElement("span");
    content.innerHTML = data[i]["content"].replace(/<\/?[^>]+(>|$)/g, " ");
    $(content).appendTo(td3);
    $(td3).appendTo(d);

    td = document.createElement("td");
    a = document.createElement("a");
    a.href=data[i]["linkName"];
    a.innerHTML = data[i]["linkName"];
    $(a).appendTo(td);
    $(td).appendTo(d);


    //$(title).appendTo(d);
    //$(content).appendTo(d);


    $(d).addClass("ele").appendTo("#data_table");

  }


}