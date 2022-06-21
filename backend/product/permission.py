
from rest_framework import permissions


# class IsStaffEditPermission(permissions.DjangoModelPermissions):
        # ''' this two are the basic two permission '''
#     def has_permission(self, request, view):
#         return super().has_permission(request, view)
        
#     def has_object_permission(self, request, view, obj):
#         return super().has_object_permission(request, view, obj)


# class isStaffHasViewPermission(permissions.DjangoModelPermissions):
#     def has_permission(self, request, view):
#         if request.user.is_staff:
#             return super().has_permission(request, view)
#         else:
#             return False


''' defining the all django model permission with help of the has_permission method and has_perm '''
class IsUserHavePermmision(permissions.DjangoModelPermissions):
    
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    
    def has_permission(self,request,view):
        user = request.user
        if not user.is_staff:
            return False
        return super().has_permission(request,view)
        
        

    
    
    
    # this view will retur true if the one of the permission is retur true
    # def has_permission(self,request,view):
        
    #     user = request.user
        
    #     if user.has_perm('product.add_product'): # 'appName.verb(action).modelName' => should in double or single quates
    #         return True
    #     if user.has_perm('product.view_product'):
    #         return True
    #     if user.has_perm('product.edit_product'):
    #         return True
    #     if user.has_perm('product.delete_product'):
    #         return True 
    #     return False
            
        
