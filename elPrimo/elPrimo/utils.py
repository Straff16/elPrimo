def loginRequired(view):
    def Isloged(request):
        if 'username' in request.session:
            view()
            return True
        else:
            return Isloged