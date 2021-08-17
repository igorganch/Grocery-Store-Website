


     function cartInc(id){
         fetch("/cart/cart_increment/" + parseInt(id) +"/").then(function(data){

            console.log("It worked")
        });
    }

  
    function uuidv4() {
		return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
		        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
		        return v.toString(16);
              });
	}

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    let device= getCookie('device');


    if (device == null || device == undefined){
        device = uuidv4();
    }
    document.cookie ='device=' + device + ";domain=;path=/";







$(document).ready(function(){

    $('.btneg').click(function(e){
        e.preventDefault();
        var decrement_value = $(this).parents('.quantity-input').find('.quantity').val();
        decrement_value = isNaN(decrement_value) ? 0 : decrement_value;

        if (decrement_value > 0 ){
            decrement_value--;
            $(this).parents('.quantity-input').find('.quantity').val(decrement_value)


        }


    });


    $('.btpos').click(function(e){
        e.preventDefault();
        var increment_value = $(this).parents('.quantity-input').find('.quantity').val();
        increment_value = isNaN(increment_value) ? 0 : increment_value;

        if (increment_value < 100 ){
            increment_value++;
            $(this).parents('.quantity-input').find('.quantity').val(increment_value)
        }
    });







    $('.btneg-cart').click(function(e){
        e.preventDefault();
        var decrement_value = $(this).parents('.quantity-input').find('.quantity').val();
        decrement_value = isNaN(decrement_value) ? 0 : decrement_value;
        var id = $(this).attr("id");
        console.log(id);
        var item_total= "#" + id +"item-total";
        var item_price = "#" + id + "-price";
        var list = "#" + id + "-list";
        if (decrement_value > 0 ){
            decrement_value--;
            $(this).parents('.quantity-input').find('.quantity').val(decrement_value)


            $.ajax({url : "/cart/cart_decrement/" + parseInt(id) +"/" , success : function(){
                
                total1 = $(item_total).text()
                total1 = parseFloat(total1.slice(1,total1.length));
                console.log(total1)
                    
                item_price = $(item_price).text();
                item_price = parseFloat(item_price.slice(1,item_price.length));
                $(item_total).text("$" + (total1 - item_price).toFixed(2));

                total2 = $("#cart-total").text();
                total2 = parseFloat(total2.slice(1,total2.length));
                $("#cart-total").text("$" + (total2 - item_price).toFixed(2));
                

            
                if (decrement_value ==0){
                    $(list).remove();
                }



            }})


        }




    });

    $('.btpos-cart').click(function(e){
        e.preventDefault();
        var increment_value = $(this).parents('.quantity-input').find('.quantity').val();
        increment_value = isNaN(increment_value) ? 0 : increment_value;

        var id = $(this).attr("id");

        var item_total= "#" + id +"item-total";
        var item_price = "#" + id + "-price";
        var list = "#" + id + "-list";


        if (increment_value < 100 ){
            increment_value++;
            $(this).parents('.quantity-input').find('.quantity').val(increment_value)

            $.ajax({url : "/cart/cart_increment/" + parseInt(id) +"/" , success : function(){
                
                total1 = $(item_total).text()
                total1 = parseFloat(total1.slice(1,total1.length));
                
                item_price = $(item_price).text();
                item_price = parseFloat(item_price.slice(1,item_price.length));
                $(item_total).text("$" + (total1 + item_price).toFixed(2));


                total2 = $("#cart-total").text();
                total2 = parseFloat(total2.slice(1,total2.length));
                $("#cart-total").text("$" + (total2 + item_price).toFixed(2));
            

                


            }})








        }
    });


    $('#myModal').on('shown.bs.modal', function () {
        console.log("FUCK");
        $('#myInput').trigger('focus')
      });




    $('.remove').click(function(e){
        
        e.preventDefault();
        var id = $(this).val();
        console.log(id);

        var list = "#" + id + "-list";
        console.log(list);

        var item_total= "#" + id +"item-total"
        $.ajax({url: "/cart/remove/" + parseInt(id) +"/",  success : function(result){
            console.log("in here");
            total1 = $(item_total).text()
            total1 = parseFloat(total1.slice(1,total1.length));
            console.log(total1)

            total2 = $("#cart-total").text();
            total2 = parseFloat(total2.slice(1,total2.length));
            
            $("#cart-total").text("$" + (total2 - total1).toFixed(2));
            

            $(list).remove();
             
            

        }});

    })




   $("form.cartform").submit(function(e){

        e.preventDefault();
        var product = $(this);
        var url =  product.attr('action');
        var data = product.serialize();
        console.log("fucking hell ll ")
        $.post(url, data, function(res){

            
    })

      

    });







});

