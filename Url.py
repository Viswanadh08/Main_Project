from django.urls import path
fromadminapp import views

urlpatterns = [
path(&#39;login/&#39;,views.admin_login, name=&#39;admin_login&#39;),
path(&#39;dashboard/&#39;,views.dashboard, name=&#39;dashboard&#39;),
path(&#39;pending-users&#39;,views.pending_users, name=&#39;pending-users&#39;),
path(&#39;accept-user/&lt;int:id&gt;/&#39;,views.accept_user, name=&#39;accept-user&#39;),
path(&#39;reject-user/&lt;int:id&gt;/&#39;,views.reject_user, name=&#39;reject-user&#39;),
path(&#39;all-users/&#39;, views.all_users, name=&#39;all-users&#39;),
path(&#39;delete-user/&lt;int:id&gt;/&#39;,views.delete, name=&#39;delete_user&#39;),
path(&#39;logout/&#39;,views.logout,name=&#39;log-out&#39;),

]
