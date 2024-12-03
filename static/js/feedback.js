$("#fd").mouseenter( function(){
        
    $("#fm").toggle('slow')
})
$("#fd").mouseleave( function(){
   
    $("#fm").hide('slow')
})
$(".feedback").click( function(){
    $("#feedback").toggle('slow')
   
})


$("#submit").click( function(){
    const name = $("#name").val()
    const occupation = $("#occupation").val()
    const photo = $("#photo")[0].files[0];
    const message = $("#message").val()

    if(name == "" || occupation =="" || message == ""){
        if(name == ""){
            $("#name").addClass('border border-red-500') 
        }else{
            $("#name").removeClass('border border-red-500')
        }

        if(occupation == ""){
            $("#occupation").addClass('border border-red-500') 
        }else{
            $("#occupation").removeClass('border border-red-500')
        }

        if(message == ""){
            $("#message").addClass('border border-red-500') 
        }else{
            $("#message").removeClass('border border-red-500')
        }
    }else{
        const FormalItem = localStorage.getItem('feedbacks');
        let list;

        if(FormalItem === null){
            list = [];
        }else{
            list = JSON.parse(FormalItem);
        }
        
        reader = new FileReader();
        
        reader.onload = function(event){
            const baseImage = event.target.result
            let feedback = [name, occupation, baseImage, message]

            list.push(feedback);

            localStorage.setItem('feedbacks', JSON.stringify(list));
        };
        reader.readAsDataURL(photo)

        $("#feedback").toggle('slow')
        $("#name").val("")
        $("#occupation").val("")
        $("#photo").val("")
        $("#message").val("")
         

    }
})

const feedback = JSON.parse(localStorage.getItem('feedbacks'));
	if(feedback != null){
		$(".carousel-testimony").empty()
        var num = 0
		feedback.forEach(item =>{
			num ++
			$(".carousel-testimony").append(
				`
				    <div class="item shadow bg-white rounded-xl p-4 border h-[400px]">
						<div class="testimony-wrap py-4">
							<div
								class="absolute top-0 right-10 z-auto bg-primary h-10 w-10 flex items-center justify-center rounded-b-lg">
								<span class="text-white text-center">${num}</span>
							</div>
							<div class="text">
								<div class="flex items-center">
									<div class="bg-cover bg-center h-28 w-28"
										style="background-image: url(${item[2]})"></div>
									<div class="pl-3">
										<p class="text-md font-sans font-semibold">${item[0]}</p>
										<span class="text-sm font-sans">${item[1]}</span>
									</div>
								</div>
								<p class="mt-4 font-sans">${item[3]}</p>
							</div>
						</div>
					</div>
				`
			)
		})
	}