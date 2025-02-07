# from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

# SignOut
from django.contrib.auth import logout

# SignUp
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Models
from .models import *

# SignIn
from django.contrib.auth import authenticate
from django.contrib.auth import login

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class WorkerSignUpView(TemplateView):
    template_name = 'worker-sign-up.html'

    def post(self, request):
        msg = {
            'username_already_taken': 'O nome de usuário já existe.',
            'user_email_already_taken': 'Já há uma conta registrada com esse e-mail.',
            'passwords_do_not_match': 'Senha inicial e de confirmação, não são idênticas!',
            'sign-up-successful': '{account_} Seu cadastro foi realizado!'
        }

        conditions = {
            # 'passwords_are_!=': str(request.POST['password']) != str(request.POST['password_confirm']),
            'username_taken': User.objects.filter(username=request.POST['username']).exists(),
            # 'email_taken': User.objects.filter(email=request.POST['email']).exists()
        }

        # If button on the form was clicked and its type is "post"
        if str(request.method) == 'POST':

            # Senhas ==
            # if conditions['passwords_are_!=']:
            #     messages.error(request, msg['passwords_do_not_match'])
            #     return redirect('sign-up')

            # Usuário já existe
            if conditions['username_taken']:
                messages.error(request, msg['username_already_taken'])
                return redirect('sign-up')

            # Email já existe
            # if conditions['email_taken']:
            #     messages.error(request, msg['user_email_already_taken'])
            #     return redirect('sign-up')

            # Tudo ok
            if True not in tuple(conditions.values()):
                new_user = User.objects.create_user(
                    # first_name=request.POST['first_name'],
                    # last_name=request.POST['last_name'],
                    username=request.POST['username'],
                    # email=request.POST['email'],
                    password=request.POST['password']
                )

                # Como "new_user" é um objeto do modelo "User", o método "save()" o salva como objeto de "User"
                new_user.save()
                messages.success(request, msg['sign-up-successful'].format(account_=new_user.get_full_name()))
                return redirect('index')

    def get_context_data(self, **kwargs):
        context = super(WorkerSignUpView, self).get_context_data(**kwargs)
        return context

class WorkerMenuView(TemplateView):
    template_name = 'worker-menu.html'

    def get_context_data(self, **kwargs):
        context = super(WorkerMenuView, self).get_context_data(**kwargs)
        context['test'] = 'Teste'
        return context

class WorkerSignInView(TemplateView):
    template_name = 'worker-sign-in.html'

    def post(self, request):
        msg = {
            'logged_in': 'Login efetuado com sucesso!',
            'incorrect_data': 'Usuário ou senha incorretas'
        }

        if str(request.method) == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Retorno: True ou None
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, msg['logged_in'])
                return redirect('index')
            if not user:
                messages.error(request, msg['incorrect_data'])
                return redirect('index')

    def get_context_data(self, **kwargs):
        context = super(WorkerSignInView, self).get_context_data(**kwargs)
        return context

class WorkerAddClientView(TemplateView):
    template_name = 'worker-add-client.html'
    message_alert = False

    def checkUserRepeated(self, client_name: str) -> bool:
        try:
            userVerification = Costumer.objects.get(full_name=client_name)
            return True if userVerification is not None else False
        except Costumer.DoesNotExist:
            return False

    def post(self, request):
        if str(request.method) == 'POST':
            newClient: Costumer = Costumer(
                full_name=request.POST.get('full_name'),
                address=request.POST.get('address'),
                neighborhood=request.POST.get('neighborhood'),
                phone=request.POST.get('phone')
            )

            newClient.save()
            WorkerAddClientView.message_alert = True
            # messages.success(request, 'Novo cliente cadastrado!')
        
        return redirect('worker-menu')

    def get_context_data(self, **kwargs):
        context = super(WorkerAddClientView, self).get_context_data(**kwargs)
        context['my_message'] = 'Novo cliente cadastrado' if WorkerAddClientView.message_alert is True else ''
        return context

class WorkerAddOrderView(TemplateView):
    template_name = 'worker-add-order.html'
    query_result = None

    def post(self, request):
        if request.method == "POST":
            print("===== RESULTADO =====")
            print(request.POST.get("orders_list"))
            print(request.POST.get("sizes_list"))
            print(request.POST.get("order_bill"))
            print(Costumer.objects.get(costumer_id=request.POST.get("client_owner")))

            newOrder: ClientOrder = ClientOrder(
                orders_list=request.POST.get("orders_list"),
                sizes_list=request.POST.get("sizes_list"),
                order_bill=request.POST.get("order_bill"),
                client_owner=Costumer.objects.get(costumer_id=request.POST.get("client_owner"))
            )
            print(newOrder.__dict__)
            newOrder.save()
            # print(request.POST.get('costumer_id'))
            # WorkerAddOrderView.query_result = Costumer.objects.filter(full_name=request.POST.get('costumer_id'))

        return redirect('order-entries')

    def get_context_data(self, **kwargs):
        context = super(WorkerAddOrderView, self).get_context_data(**kwargs)
        context['all_costumers'] = Costumer.objects.all()
        context['all_categories'] = Category.objects.all()
        # context['query_result'] = len(WorkerAddOrderView.query_result)
        return context

class WorkerEntriesView(TemplateView):
    template_name = 'order-entries.html'

    def get_context_data(self, **kwargs):
        context = super(WorkerEntriesView, self).get_context_data(**kwargs)
        context['each_order'] = ClientOrder.objects.all()
        return context

def sign_out(request):
    messages.success(request, 'Deslogando...')
    logout(request)
    return redirect('index')
