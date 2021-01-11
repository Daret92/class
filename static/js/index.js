$(document).ready(function(){
    $('#tablaProduc').DataTable();

    $('.totalProduct').on("input",function(){
        if( $(this).val() > parseFloat($(this).data("maxp"))){
            $(this).val(parseFloat($(this).data("maxp")))
        }
    });
    $('.closesMessage').click(function(){
        $("#mensajes").addClass("hiddens");
    });

    $('.addCar').on("click",function(){
        var totalproduct = $(this).parent().parent().find(".totalProduct");
        $.ajax({
            //data:{
              //  total:totalproduct,
               // pk:$(this).data("idproduct")
            //},
            type:'GET',
            //dataType:'json',
            url:'/add_car_user?total_product='+totalproduct.val()+
            '&&pk_product='+$(this).data("idproduct"),
            success:function(request){
                if(request["success"]==true){                        
                    var tabla = document.querySelector("#tabla");
                    if(tabla == null){
                        
                        var newTable = document.createElement("table");
                        newTable.setAttribute("id","tabla");
                        newTable.setAttribute("class","table");
                        
                        var newTHead = document.createElement("thead");
                        
                        var TrHead = document.createElement("tr");
                        
                        var thHead0 = document.createElement("th");
                        thHead0.innerHTML = "Producto";
                        
                        var thHead1 = document.createElement("th");
                        thHead1.innerHTML = "Cantidad";
                        TrHead.appendChild(thHead0);
                        TrHead.appendChild(thHead1);
                        newTHead.appendChild(TrHead);
                        newTable.appendChild(newTHead);
                        
                        var newTBody = document.createElement("tbody");        
                        newTBody.setAttribute("id","car_productos");
                        newTable.appendChild(newTBody);
                        
                        var divTable = document.querySelector("#innerTable");
                        divTable.appendChild(newTable);
                    }
                    var trDelete = document.getElementsByClassName(request["pk_producto"]+"_producto");
                    trDelete[0].remove();

                    var trTable = document.createElement("TR");//<tr></tr>
                    trTable.setAttribute("class",request["pk_producto"].toString()+"_producto"); //<tr class="id_producto"></tr>
                    
                    var tdTableName = document.createElement("TD");//<td></td>
                    tdTableName.setAttribute("class","car_name");//<td class="car_name"></td>
                    tdTableName.innerHTML = request["name"];//<td class="car_name">name</td>
                    
                    var tdTableTotal = document.createElement("TD");//<td></td>
                    tdTableTotal.setAttribute("class","car_product");//<td class="car_total"></td>
                    tdTableTotal.innerHTML = parseFloat(request["total"]);//<td class="car_total">total</td>
                    

                    trTable.appendChild(tdTableName);//<tr class="id_producto"><td class="car_name">name</td><tr/>
                    trTable.appendChild(tdTableTotal);//<tr class="id_producto"><td class="car_name">name</td><td class="car_total">total</td><tr/>

                    var tbody = document.querySelector("#car_productos");//<tbody id="car_productos"></tbody>

                    tbody.appendChild(trTable);//<tbody id="car_productos">
                                                //<tr class="id_producto"><td class="car_name">name</td><td class="car_total">total</td><tr/>
                                                //</tbody>   
                }else{
                    var mensaje = document.getElementById("mensajes");
                    mensaje.removeAttribute("class");
                    var showMensaje = document.getElementById("mensajeId");
                    showMensaje.innerHTML = request["mensaje"];
                }
            },
            error:function(xhr,err){
                console.log(xhr.error);
                console.log(err);
            },
            complete:function(xhr,status){
                totalproduct.val("");
            }

        })
    });
    $(".remove").on("click",function(){
        alert($(this).data("idproduct"))
    });

});