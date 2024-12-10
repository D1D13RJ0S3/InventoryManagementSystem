<!--
Component: UpdateButton.svelte
Description: This component provides a button to update a selected product.
It handles the update process, including validation, confirmation dialogs, and error alerts.
Properties:
  - selectedProducts (Set): A set of selected product IDs for updating.
  - selectedProduct (object): The selected product object to be updated.
Internal Variables:
  - showUpdateDialog (boolean): Controls the visibility of the update dialog.
  - showAlert (boolean): Controls the visibility of the alert when invalid selections are made.
  - updatedData (object): Stores the updated data for the product.
  - currentData (object): Stores the current data of the product before updating.
Main Functions:
  - openUpdateDialog(): Opens the update dialog if exactly one product is selected.
  - confirmUpdate(): Validates and sends the updated data to the backend.
  - cancelUpdate(): Cancels the update process and closes the dialog.
  - getProductNameById(id): Retrieves the product name by its ID.
External Dependencies:
  - Requires a backend at `http://localhost:5000` to handle update requests.
-->
<script>
  import { createEventDispatcher } from 'svelte';

  export let selectedProducts; // Set of selected product IDs
  export let selectedProduct = null; // Selected product object

  const dispatch = createEventDispatcher();
  let showUpdateDialog = false;
  let showAlert = false;
  let updatedData = {}; // Object to store updated data
  let currentData = {}; // Object to store current product data

  function openUpdateDialog() {
    if (selectedProducts.size === 1 && selectedProduct) { // Ensure only one product is selected and data exists
      updatedData = { ...selectedProduct }; // Copy selected product data for editing
      currentData = { ...selectedProduct }; // Store current product data
      showUpdateDialog = true;
    } else {
      showAlert = true;
      setTimeout(() => (showAlert = false), 3000);
    }
  }

  async function confirmUpdate() {
    if (updatedData.price < 0 || updatedData.quantity < 0) {
      console.error('The product values are invalid');
      return;
    }

    try {
      const productId = selectedProduct.id; // Get the selected product ID
      const response = await fetch(`http://localhost:5000/update/${productId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error updating product with ID ${productId}:`, errorData);
        throw new Error(errorData.detail || 'Error updating the product');
      }

      dispatch('updateSuccess', { id: productId, ...updatedData }); // Emit event with updated data
      selectedProducts.clear();
      updatedData = {}; // Reset form data
      showUpdateDialog = false;
    } catch (error) {
      console.error('Update error:', error.message || error);
    }
  }

  function cancelUpdate() {
    showUpdateDialog = false;
    updatedData = {}; // Reset form data
  }

  // Function to get the product name by ID
  function getProductNameById(id) { 
    console.log("Searching for product with ID:", id); 
    console.log("Available products:", selectedProduct); 
    const product = selectedProduct; // Assuming selectedProduct is the current product
    if (!product) { console.error("Product not found for ID:", id); } 
    return product?.name || 'Unknown'; 
  }
</script>

<!-- Decorative "Update Product" Button -->
<button class="button" on:click={openUpdateDialog} disabled={selectedProducts.size !== 1}>
  <span class="button__text">Actualizar</span>
  <span class="button__icon">
    <svg class="svg" height="48" viewBox="0 0 48 48" width="48" xmlns="http://www.w3.org/2000/svg">
      <path d="M35.3 12.7c-2.89-2.9-6.88-4.7-11.3-4.7-8.84 0-15.98 7.16-15.98 16s7.14 16 15.98 16c7.45 0 13.69-5.1 15.46-12h-4.16c-1.65 4.66-6.07 8-11.3 8-6.63 0-12-5.37-12-12s5.37-12 12-12c3.31 0 6.28 1.38 8.45 3.55l-6.45 6.45h14v-14l-4.7 4.7z"></path>
      <path d="M0 0h48v48h-48z" fill="none"></path>
    </svg>
  </span>
</button>

{#if showAlert}
  <div class="alert">
    You must select exactly one product to update.
  </div>
{/if}

{#if showUpdateDialog}
  <div class="popup-overlay">
    <div class="popup-content">
      <h3>Update</h3>
      <form on:submit|preventDefault={confirmUpdate}>
        <label for="name">Name:</label>
        <input 
          type="text" 
          id="name" 
          bind:value={updatedData.name} 
          placeholder="New name"
          required
        >
        <span>(Current: {currentData.name})</span>

        <label for="price">Price:</label>
        <input 
          type="number" 
          id="price" 
          bind:value={updatedData.price} 
          min="0" 
          placeholder="New price"
          required
        >
        <span>(Current: {currentData.price})</span>

        <label for="quantity">Quantity:</label>
        <input 
          type="number" 
          id="quantity" 
          bind:value={updatedData.quantity} 
          min="0" 
          placeholder="New quantity"
          required
        >
        <span>(Current: {currentData.quantity})</span>

        <div class="popup-actions">
          <button type="button" on:click={cancelUpdate}>Cancelar</button>
          <button type="submit">Actualizar</button>
        </div>
      </form>
    </div>
  </div>
{/if}

<style>
  .alert {
    background-color: #f44336;
    color: white;
    padding: 10px;
    border-radius: 5px;
    margin-top: 10px;
    text-align: center;
    z-index: 1001; /* Optional: Ensures alerts are above other elements */
  }

  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000; /* Ensures the popup is above other elements */
  }

  .popup-content {
    background: #fff;
    padding: 20px 30px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
    text-align: center;
    width: 400px;
  }

  .popup-actions button {
    margin: 10px 5px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .popup-actions button:first-child {
    background-color: #f4f4f4;
  }

  .popup-actions button:last-child {
    background-color: #4caf50;
    color: #fff;
  }

  .popup-content label {
    display: block;
    margin-top: 15px;
    font-weight: bold;
  }

  .popup-content input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    margin-bottom: 5px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }

  .popup-content span {
    display: block;
    margin-bottom: 15px;
    color: #888;
    font-size: 0.9em;
  }

  /* Styles for the Decorative Button */
  .button {
    --main-focus: #2d8cf0;
    --font-color: #323232;
    --bg-color-sub: #dedede;
    --bg-color: #eee;
    --main-color: #323232;
    position: relative;
    width: 150px;
    height: 40px;
    cursor: pointer;
    display: flex;
    align-items: center;
    border: 2px solid var(--main-color);
    box-shadow: 4px 4px var(--main-color);
    background-color: var(--bg-color);
    border-radius: 10px;
    overflow: hidden;
    transition: background 0.3s, transform 0.1s, box-shadow 0.1s;
    padding: 0;
    outline: none;
  }

  .button:hover {
    background: var(--bg-color);
  }

  .button:hover .button__text {
    color: transparent;
  }

  .button:hover .button__icon {
    width: 148px;
    transform: translateX(0);
  }

  .button:active {
    transform: translate(3px, 3px);
    box-shadow: 0px 0px var(--main-color);
  }

  .button__text {
    transform: translateX(30px); /* Adjusted according to the previous code */
    color: var(--font-color);
    font-weight: 600;
    pointer-events: none;
    transition: all 0.3s;
  }

  .button__icon {
    position: absolute;
    transform: translateX(109px); /* Adjusted according to the previous code */
    height: 100%;
    width: 39px;
    background-color: var(--bg-color-sub);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
  }

  .svg {
    width: 20px;
    fill: var(--main-color);
    transition: all 0.3s;
  }

  /* Disable button when disabled */
  .button:disabled {
    cursor: not-allowed;
    opacity: 0.6;
  }
</style>