from m3_ext.ui import all_components as ext

from objectpack.ui import BaseEditWindow


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label='Password',
            name='password',
            allow_blank=False,
            anchor='100%'
        )
        self.field__username = ext.ExtStringField(
            label='Username',
            name='username',
            allow_blank=False,
            anchor='100%'
        )
        self.field__first_name = ext.ExtStringField(
            label='First name',
            name='first_name',
            allow_blank=True,
            anchor='100%'
        )
        self.field__last_name = ext.ExtStringField(
            label='Last name',
            name='last_name',
            allow_blank=True,
            anchor='100%'
        )
        self.field__email = ext.ExtStringField(
            label='Email',
            name='email',
            allow_blank=True,
            anchor='100%'
        )
        self.field__date_joined = ext.ExtDateField(
            label='Date joined',
            name='date_joined',
            allow_blank=True,
            anchor='100%'
        )
        self.field__last_login = ext.ExtDateField(
            label='Last login',
            name='last_login',
            allow_blank=True,
            anchor='100%'
        )
        self.field__is_active = ext.ExtCheckBox(
            label='Active?',
            name='is_active',
            allow_blank=False,
            anchor='100%'
        )
        self.field__is_staff = ext.ExtCheckBox(
            label='Staff?',
            name='is_staff',
            allow_blank=False,
            anchor='100%'
        )
        self.field__is_superuser = ext.ExtCheckBox(
            label='superuser status',
            name='is_superuser',
            allow_blank=False,
            anchor='100%'
        )

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__date_joined,
            self.field__last_login,
            self.field__is_superuser,
            self.field__is_staff,
            self.field__is_active,
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


