<script>
  import { onMount, onDestroy } from 'svelte';
  import ProductList from '../components/FunctionPages/ProductList.svelte';
  import DeleteButton from '../components/APIFunctions/DeleteButton.svelte';
  import CreateProductPopup from '../components/APIFunctions/CreateProductPopup.svelte';
  import UpdateButton from '../components/APIFunctions/UpdateButton.svelte';
  import SearchBar from '../components/Buttons/SearchBar.svelte';
  import { formatToCOP } from '../lib/utils.js'; // Import formatting function

  let searchTerm = ''; 
  let isPopupOpen = false; 
  let selectedProducts = new Set(); 
  let productos = []; 
  let selectedProduct = null;
  let filteredProducts = []; 
  let refreshInterval = null; 
  let totalInventoryValue = 0; // New variable for total inventory value

  // Compute the selected product
  $: selectedProduct = selectedProducts.size === 1 
    ? productos.find(p => p.id === Array.from(selectedProducts)[0]) 
    : null;

  // Calculate total inventory value whenever filteredProducts change
  $: totalInventoryValue = filteredProducts.reduce((sum, product) => {
    return sum + (product.quantity * product.price);
  }, 0);

  /**
   * Fetches products from the API and updates the product list.
   */
  async function fetchProducts() {
    try {
      const response = await fetch('http://localhost:5000/products');
      if (!response.ok) {
        throw new Error('Error fetching products');
      }
      productos = await response.json();
      productos = [...productos]; // Force reactivity
      filterProducts();
    } catch (error) {
      console.error('Error:', error);
    }
  }

  /**
   * Filters the products based on the search term.
   */
  function filterProducts() {
    if (!searchTerm) {
      filteredProducts = productos;
    } else {
      const lowerSearchTerm = searchTerm.toLowerCase();
      filteredProducts = productos.filter((product) =>
        product.name.toLowerCase().includes(lowerSearchTerm)
      );
    }
    filteredProducts = [...filteredProducts]; // Force reactivity
  }

  onMount(() => {
    fetchProducts(); // Load products initially
    refreshInterval = setInterval(fetchProducts, 1400); // Refresh every 1.4 seconds

    return () => {
      clearInterval(refreshInterval); // Clear interval on destroy
    };
  });

  onDestroy(() => {
    clearInterval(refreshInterval);
  });

  /**
   * Opens the create product popup.
   */
  function openPopup() {
    isPopupOpen = true;
  }

  /**
   * Closes the create product popup.
   */
  function closePopup() {
    isPopupOpen = false;
  }

  /**
   * Handles successful deletion of products.
   * @param {Event} event - The event containing deleted product IDs.
   */
  function handleDeleteSuccess(event) {
    console.log('Product deleted, reloading products...');
    fetchProducts();
  }

  /**
   * Handles successful update of a product.
   * @param {Event} event - The event containing the updated product.
   */
  function handleUpdateSuccess(event) {
    console.log('Product updated, reloading products...');
    fetchProducts();
  }

  /**
   * Handles the submission of a new product.
   * @param {Event} event - The submit event.
   */
  function handleSubmit(event) {
    fetchProducts();
  }

  /**
   * Handles the search functionality.
   * @param {Event} event - The search event containing the search term.
   */
  function handleSearch(event) {
    searchTerm = event.detail.searchTerm; // Update the search term
    filterProducts(); // Re-filter products
  }
</script>

{#if isPopupOpen}
  <CreateProductPopup isOpen={isPopupOpen} onClose={closePopup} onSubmit={() => fetchProducts()} />
{/if}

<section class="inventory">
  <div class="title-search-container">
    <h2 class="inventory-title">Lista de Productos</h2>
    <SearchBar searchTerm={searchTerm} on:search={handleSearch} />
  </div>
  

  <!-- Fixed Header with classes for defined widths -->
  <div class="header">
    <div class="select-column">Seleccionar</div>
    <div class="name-column">Nombre</div>
    <div class="quantity-column">Cantidad</div>
    <div class="price-column">Precio</div>
    <div class="total-column">Total</div> <!-- New Total column -->
  </div>

  <!-- Scrollable product list -->
  <div class="product-list">
    <ProductList {filteredProducts} bind:selectedProducts />
  </div>

  <!-- Total Inventory Value Box -->
  <div class="total-inventory">
    Valor Total Inventario: {formatToCOP(totalInventoryValue)}
  </div>

  <div class="buttons-container">
    <CreateProductPopup onSubmit={handleSubmit} />
    <UpdateButton 
      bind:selectedProducts 
      {selectedProduct} 
      on:updateSuccess={handleUpdateSuccess} 
    />
    <DeleteButton products={productos} bind:selectedProducts on:deleteSuccess={handleDeleteSuccess} />
  </div>
</section>

<style>
  
  * {
    box-sizing: border-box;
  }

  .title-search-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px; /* Spacing below the container */
}
  /* Container for the entire inventory page */
  .inventory {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
 
  
  
  /* Inventory title */
  .inventory-title {
    text-align: center;
    margin-bottom: 20px;
  }

  
  .header {
    display: flex;
    background-color: #f4f4f4; /* Background color similar to th */
    border-bottom: 1px solid #ddd; /* Only bottom border */
    position: sticky;
    top: 0;
    z-index: 10;
  }
  
  .header div {
    padding: 10px; 
    text-align: left;
    border-right: 1px solid #ddd;
    font-weight: bold;
  }
  
  .header div:last-child {
    border-right: none;
  }
  
  
  .select-column {
    width: 10%;
  }
  
  .name-column {
    width: 30%; 
  }
  
  .quantity-column {
    width: 15%; 
  }
  
  .price-column {
    width: 15%; 
  }
  
  .total-column {
    width: 30%; 
  }
  
  /* Scrollable product list */
  .product-list {
    max-height: 280px;
    overflow-y: auto;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #f9f9f9;
  }

  /* Total Inventory Value Box */
  .total-inventory {
    margin-top: 20px;
    padding: 15px;
    background-color: #e0e0e0;
    text-align: center;
    font-weight: bold;
    font-size: 1.2em;
    border-radius: 8px;
  }
  
  /* Buttons container */
  .buttons-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-top: 20px;
  }
  
 
  .product-list::-webkit-scrollbar {
    width: 8px;
  }
  
  .product-list::-webkit-scrollbar-thumb {
    background-color: rgba(0, 0, 0, 0.2);
    border-radius: 4px;
  }
</style>
