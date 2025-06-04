// Hamburger menu toggle (your existing code)
const hamburger = document.getElementById('hamburger');
const nav = document.getElementById('navbar');

hamburger.addEventListener('click', () => {
  const expanded = hamburger.getAttribute('aria-expanded') === 'true';
  hamburger.setAttribute('aria-expanded', !expanded);
  hamburger.classList.toggle('active');
  nav.classList.toggle('show');
});
hamburger.addEventListener('keydown', e => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault();
    hamburger.click();
  }
});



// Slider logic (existing, keep as is)
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.slider-dot');
let currentSlide = 0;

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.toggle('active', i === index);
    slide.setAttribute('aria-hidden', i !== index);
    dots[i].classList.toggle('active', i === index);
    dots[i].setAttribute('aria-selected', i === index);
    dots[i].tabIndex = i === index ? 0 : -1;
  });
  currentSlide = index;
}

dots.forEach((dot, i) => {
  dot.addEventListener('click', () => showSlide(i));
  dot.addEventListener('keydown', e => {
    if(e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      showSlide(i);
    }
  });
});

setInterval(() => {
  let next = (currentSlide + 1) % slides.length;
  showSlide(next);
}, 6000);





// Products array with 9 local images per category
const products = [
  // Shoes
  { id: 1, Name: "Product 1", Category: "Shoes", Price: 129.99, ImageURL: "images/product_1.jpg" },
  { id: 2, Name: "Product 2", Category: "Shoes", Price: 139.99, ImageURL: "images/product_2.jpg" },
  { id: 3, Name: "Product 3", Category: "Shoes", Price: 119.99, ImageURL: "images/product_3.jpg" },
  { id: 4, Name: "Product 4", Category: "Shoes", Price: 149.99, ImageURL: "images/product_4.jpg" },
  { id: 5, Name: "Product 5", Category: "Shoes", Price: 99.99, ImageURL: "images/product_5.jpg" },
  { id: 6, Name: "Product 6", Category: "Shoes", Price: 109.99, ImageURL: "images/product_6.jpg" },
  { id: 7, Name: "Product 7", Category: "Shoes", Price: 129.99, ImageURL: "images/product_7.jpg" },
  { id: 8, Name: "Product 8", Category: "Shoes", Price: 159.99, ImageURL: "images/product_8.jpg" },
  { id: 9, Name: "Product 9", Category: "Shoes", Price: 139.99, ImageURL: "images/product_9.jpg" },

  // Apparel
  { id: 10, Name: "Apparel 1", Category: "Apparel", Price: 59.99, ImageURL: "images/apparel_1.jpg" },
  { id: 11, Name: "Apparel 2", Category: "Apparel", Price: 69.99, ImageURL: "images/apparel_2.jpg" },
  { id: 12, Name: "Apparel 3", Category: "Apparel", Price: 79.99, ImageURL: "images/apparel_3.jpg" },
  { id: 13, Name: "Apparel 4", Category: "Apparel", Price: 89.99, ImageURL: "images/apparel_4.jpg" },
  { id: 14, Name: "Apparel 5", Category: "Apparel", Price: 59.99, ImageURL: "images/apparel_5.jpg" },
  { id: 15, Name: "Apparel 6", Category: "Apparel", Price: 69.99, ImageURL: "images/apparel_6.jpg" },
  { id: 16, Name: "Apparel 7", Category: "Apparel", Price: 79.99, ImageURL: "images/apparel_7.jpg" },
  { id: 17, Name: "Apparel 8", Category: "Apparel", Price: 89.99, ImageURL: "images/apparel_8.jpg" },
  { id: 18, Name: "Apparel 9", Category: "Apparel", Price: 99.99, ImageURL: "images/apparel_9.jpg" },

  // Accessories
  { id: 19, Name: "Accessory 1", Category: "Accessories", Price: 19.99, ImageURL: "images/accessory_1.jpg" },
  { id: 20, Name: "Accessory 2", Category: "Accessories", Price: 24.99, ImageURL: "images/accessory_2.jpg" },
  { id: 21, Name: "Accessory 3", Category: "Accessories", Price: 29.99, ImageURL: "images/accessory_3.jpg" },
  { id: 22, Name: "Accessory 4", Category: "Accessories", Price: 14.99, ImageURL: "images/accessory_4.jpg" },
  { id: 23, Name: "Accessory 5", Category: "Accessories", Price: 34.99, ImageURL: "images/accessory_5.jpg" },
  { id: 24, Name: "Accessory 6", Category: "Accessories", Price: 39.99, ImageURL: "images/accessory_6.jpg" },
  { id: 25, Name: "Accessory 7", Category: "Accessories", Price: 44.99, ImageURL: "images/accessory_7.jpg" },
  { id: 26, Name: "Accessory 8", Category: "Accessories", Price: 22.99, ImageURL: "images/accessory_8.jpg" },
  { id: 27, Name: "Accessory 9", Category: "Accessories", Price: 27.99, ImageURL: "images/accessory_9.jpg" }
];



// Category filter buttons
const categoryButtons = document.querySelectorAll('.category-btn');
categoryButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    categoryButtons.forEach(b => {
      b.classList.remove('active');
      b.setAttribute('aria-pressed', 'false');
    });
    btn.classList.add('active');
    btn.setAttribute('aria-pressed', 'true');

    const cat = btn.getAttribute('data-category');
    renderProducts(cat);
  });
});

// Render products function
function renderProducts(category = 'all') {
  const container = document.getElementById('featured-products');
  container.innerHTML = '';
  let filtered = category === 'all' ? products : products.filter(p => p.Category === category);
  if(filtered.length === 0){
    container.innerHTML = '<p style="text-align:center; color:#666;">No products found in this category.</p>';
    return;
  }
  filtered.forEach(p => {
    const card = document.createElement('article');
    card.className = 'product-card';
    card.tabIndex = 0;
    card.dataset.id = p.id;

    card.innerHTML = `
      <img loading="lazy" class="product-image" src="${p.ImageURL}" alt="${p.Name}" />
      <div class="product-info">
        <h3 class="product-name">${p.Name}</h3>
        <p class="product-desc">${p.Category}</p>
        <div class="product-price">$${p.Price.toFixed(2)}</div>
        <button class="add-cart-btn" aria-label="Add ${p.Name} to cart">Add to Cart</button>
      </div>
    `;

    card.querySelector('.add-cart-btn').addEventListener('click', () => {
      addToCart(p);
    });

    container.appendChild(card);
  });
}

// Cart management
const cartSidebar = document.getElementById('cart-sidebar');
const cartItemsContainer = document.getElementById('cart-items');
const cartTotalDisplay = document.getElementById('cart-total');
let cart = [];

function updateCartUI(){
  cartItemsContainer.innerHTML = '';
  if(cart.length === 0){
    cartItemsContainer.innerHTML = '<p>Your cart is empty.</p>';
    cartTotalDisplay.textContent = 'Total: $0.00';
    cartSidebar.setAttribute('aria-hidden', 'true');
    return;
  }
  cart.forEach(item => {
    const div = document.createElement('div');
    div.className = 'cart-item';
    div.innerHTML = `
      <img src="${item.ImageURL}" alt="${item.Name}" />
      <div class="cart-item-info">
        <div class="cart-item-name">${item.Name}</div>
        <div class="cart-item-price">$${item.Price.toFixed(2)}</div>
        <div class="cart-item-qty">Qty: ${item.qty}</div>
      </div>
      <button aria-label="Remove ${item.Name} from cart" class="remove-cart-item">&times;</button>
    `;
    div.querySelector('.remove-cart-item').addEventListener('click', () => {
      removeFromCart(item.id);
    });
    cartItemsContainer.appendChild(div);
  });
  const total = cart.reduce((sum, item) => sum + item.Price * item.qty, 0);
  cartTotalDisplay.textContent = `Total: $${total.toFixed(2)}`;
  cartSidebar.setAttribute('aria-hidden', 'false');
}

function addToCart(product) {
  const found = cart.find(item => item.id === product.id);
  if(found){
    found.qty++;
  } else {
    cart.push({...product, qty: 1});
  }
  updateCartUI();
  openCart();
}

function removeFromCart(productId){
  cart = cart.filter(item => item.id !== productId);
  updateCartUI();
}

function openCart(){
  cartSidebar.classList.add('active');
}
function closeCart(){
  cartSidebar.classList.remove('active');
}
document.getElementById('close-cart-btn').addEventListener('click', closeCart);

// Feedback modal
const feedbackModal = document.getElementById('feedback-modal');
const feedbackForm = document.getElementById('feedback-form');
const feedbackCloseBtn = document.getElementById('close-feedback-btn');

function openFeedback(){
  feedbackModal.classList.add('active');
  feedbackModal.setAttribute('aria-hidden', 'false');
}
function closeFeedback(){
  feedbackModal.classList.remove('active');
  feedbackModal.setAttribute('aria-hidden', 'true');
}
feedbackCloseBtn.addEventListener('click', closeFeedback);
feedbackModal.addEventListener('click', e => {
  if(e.target === feedbackModal) closeFeedback();
});

// Feedback form submission
feedbackForm.addEventListener('submit', e => {
  e.preventDefault();
  const name = feedbackForm.querySelector('#name').value.trim();
  const email = feedbackForm.querySelector('#email').value.trim();
  const feedback = feedbackForm.querySelector('#feedback').value.trim();
  if(name && email && feedback){
    alert('Thank you for your feedback!');
    feedbackForm.reset();
    closeFeedback();
  } else {
    alert('Please fill in all fields.');
  }
});

// Initialize page load event to render all products
window.addEventListener('load', () => {
  renderProducts('all');
});

// Add a floating feedback button
const feedbackBtn = document.createElement('button');
feedbackBtn.textContent = 'Feedback';
feedbackBtn.style.position = 'fixed';
feedbackBtn.style.bottom = '30px';
feedbackBtn.style.left = '30px';
feedbackBtn.style.padding = '1rem 1.6rem';
feedbackBtn.style.background = 'linear-gradient(135deg, #1e90ff, #3db1ff)';
feedbackBtn.style.color = 'white';
feedbackBtn.style.borderRadius = '40px';
feedbackBtn.style.fontWeight = '700';
feedbackBtn.style.cursor = 'pointer';
feedbackBtn.style.boxShadow = '0 6px 22px rgba(30,144,255,0.6)';
feedbackBtn.style.zIndex = '100001';
feedbackBtn.setAttribute('aria-label', 'Open feedback form');
document.body.appendChild(feedbackBtn);
feedbackBtn.addEventListener('click', openFeedback);
