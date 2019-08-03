from django import forms

class RegistrationForm(forms.Form):
    firstname=forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter First Name'
            }
        )
    )
    lastname = forms.CharField(
        label="Enter Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
            }
        )
    )
    username = forms.CharField(
        label="Enter User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Name'
            }
        )
    )
    password = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            }
        )
    )
    location = forms.CharField(
        label="Enter Location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Location'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Number'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }
        )
    )


class LoginForm(forms.Form):
    username=forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"Enter Your Username"
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Password"
            }
        )
    )

class ImageForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"Enter Your Name"
            }
        )
    )
    image = forms.ImageField(
        label="Enter Your Image",
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Image"
            }
        )
    )


class Inserting_data(forms.Form):
    product_id=forms.IntegerField(
        label="Enter the product id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter the product name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Name'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter the product class",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Class'
            }
        )
    )
    product_color= forms.CharField(
        label="Enter the product color",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Color'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter the product cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )