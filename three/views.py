from django.shortcuts import render

def sounds(request):
    return render(request, "3/sound.html", {
        "title": "Challenge 3"
    })

def images(request):
    return render(request, "3/image.html", {
        "title": "Challenge 3"
    })

def video(request):
    return render(request, "3/video.html", {
        "title": "Challenge 3"
    })