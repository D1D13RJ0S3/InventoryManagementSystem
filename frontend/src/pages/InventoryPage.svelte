<!--
Component: InventoryPage.svelte
Description: This component manages the inventory page, allowing users to view, search, create, update, and delete products.
Properties:
  - None
Internal Variables:
  - searchTerm (string): The current search term entered by the user.
  - isPopupOpen (boolean): Controls the visibility of the create product popup.
  - selectedProducts (Set): A set of selected product IDs for deletion.
  - productos (array): The list of all products fetched from the API.
  - selectedProduct (object|null): The currently selected product for updates.
  - filteredProducts (array): The list of products filtered based on the search term.
  - refreshInterval (number|null): The interval ID for refreshing the product list.
Main Functions:
  - fetchProducts(): Fetches products from the API and updates the product list.
  - filterProducts(): Filters the product list based on the search term.
  - openPopup(): Opens the create product popup.
  - closePopup(): Closes the create product popup.
  - handleDeleteSuccess(event): Handles successful deletion of products.
  - handleUpdateSuccess(event): Handles successful update of a product.
  - handleSubmit(event): Handles the submission of a new product.
  - handleSearch(event): Handles the search functionality.
External Dependencies:
  - ProductList.svelte: Component to display the list of products.
  - DeleteButton.svelte: Component to handle deletion of selected products.
  - CreateProductPopup.svelte: Component to create a new product.
  - UpdateButton.svelte: Component to handle updating a selected product.
  - SearchBar.svelte: Component to handle searching/filtering products.
-->
<script>
  import { onMount, onDestroy } from 'svelte';
  import ProductList from '../components/FunctionPages/ProductList.svelte';
  // Remove the import of Button.svelte
  // import Button from '../components/Buttons/Button.svelte';
  import DeleteButton from '../components/APIFunctions/DeleteButton.svelte';
  import CreateProductPopup from '../components/APIFunctions/CreateProductPopup.svelte';
  import UpdateButton from '../components/APIFunctions/UpdateButton.svelte';
  import SearchBar from '../components/Buttons/SearchBar.svelte';

  let searchTerm = ''; 
  let isPopupOpen = false; 
  let selectedProducts = new Set(); 
  let productos = []; 
  let selectedProduct = new Set();
  let filteredProducts = []; 
  let refreshInterval = null; 

  // Compute the selected product
  $: selectedProduct = selectedProducts.size === 1 
    ? productos.find(p => p.id === Array.from(selectedProducts)[0]) 
    : null;
      
  /**
   * Fetches products from the API and updates the product list.
   */
  async function fetchProducts() {
    try {
      const response = await fetch('http://localhost:5000/products');
      if (!response.ok) {
        throw new Error('Error al obtener productos');
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
    console.log('Producto eliminado, recargando productos...');
    fetchProducts();
  }

  /**
   * Handles successful update of a product.
   * @param {Event} event - The event containing the updated product.
   */
  function handleUpdateSuccess(event) {
    console.log('Producto actualizado, recargando productos...');
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

<div class="inventory-container">
  <div class="search-bar">
    <SearchBar searchTerm={searchTerm} on:search={handleSearch} />
  </div>

  <section class="inventory">
    <h2 class="inventory-title">Productos</h2>
    <ProductList {filteredProducts} bind:selectedProducts />
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

  {#if isPopupOpen}
    <CreateProductPopup isOpen={isPopupOpen} onClose={closePopup} onSubmit={() => fetchProducts()} />
  {/if}
</div>

<style>
  /* 
    Container for the entire inventory page.
    Arranges elements vertically with spacing.
  */
  .inventory-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  /* 
    Styles for the search bar container.
    Adds padding, border, rounded corners, background color,
    centers its content, and applies a subtle box shadow.
  */
  .search-bar {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #f9f9f9;
    display: flex;
    justify-content: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  /* 
    Container for the inventory section.
    Adds padding, border, rounded corners, background color, and a subtle shadow.
  */
  .inventory {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  /* 
    Title for the inventory section.
    Centers the text and adds bottom margin.
  */
  .inventory-title {
    text-align: center;
    margin-bottom: 20px;
  }

  /* 
    Container for action buttons below the product list.
    Centers the buttons and adds spacing between them.
  */
  .buttons-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-top: 20px;
  }

  /* 
    No need to duplicate button styles here.
  */
</style>