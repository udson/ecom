from store.models import Product


class Cart():
  def __init__(self, request):
    self.session = request.session
  
    cart = self.session.get('session_key')

    if 'session_key' not in request.session:
      cart = self.session['session_key'] = {}
    
    self.cart = cart
  
  def add(self, product, quantity):
    product_id = str(product.id)
    quantity = quantity
    if product_id in self.cart:
      pass
    else:
      self.cart[product_id] = quantity
    
    self.session.modified = True
  
  def __len__(self):
    return len(self.cart)
  
  def get_prods(self):
    return {Product.objects.get(pk=k): self.cart[k] for k in self.cart.keys()}
     
  
  def get_quantities(self):
    return self.cart
