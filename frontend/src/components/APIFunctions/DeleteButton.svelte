<!--
Component: DeleteButton.svelte
Description: This component provides a button to delete selected products.
It handles the deletion process, including confirmation dialogs and error alerts.
Properties:
  - selectedProducts (Set): A set of selected product IDs for deletion.
  - products (array): Complete list of products: [{ id: 1, name: "Product A" }, ...]
Internal Variables:
  - showConfirmDelete (boolean): Controls the visibility of the confirmation dialog.
  - showAlert (boolean): Controls the visibility of the alert when no products are selected.
Main Functions:
  - openConfirmationDialog(): Opens the confirmation dialog if products are selected; otherwise, shows an alert.
  - confirmDelete(): Confirms and deletes the selected products by sending DELETE requests to the backend.
  - cancelDelete(): Cancels the deletion process and closes the confirmation dialog.
  - getProductNameById(id): Retrieves the product name by its ID.
External Dependencies:
  - Requires a backend at `http://localhost:5000` to handle deletion requests.
-->

<script>
  import { createEventDispatcher } from 'svelte';

  export let selectedProducts; // Changed to Set for consistency
  export let products = []; // Complete list of products: [{ id: 1, name: "Product A" }, ...]

  const dispatch = createEventDispatcher();
  let showConfirmDelete = false;
  let showAlert = false;

  function openConfirmationDialog() {
    if (selectedProducts.size > 0) { // Using size instead of length for Set
      showConfirmDelete = true;
    } else {
      showAlert = true;
      setTimeout(() => showAlert = false, 3000);
    }
  }

  async function confirmDelete() {
    try {
      for (const productId of selectedProducts) {
        const response = await fetch(`http://localhost:5000/delete/${productId}`, {
          method: 'DELETE',
        });

        if (!response.ok) {
          const errorData = await response.json();
          console.error(`Error deleting product with ID ${productId}:`, errorData);
          throw new Error(errorData.detail || 'Error deleting the product');
        }
      }

      dispatch('deleteSuccess', Array.from(selectedProducts)); // Emit event with an array
      selectedProducts.clear(); // Clear the Set
      showConfirmDelete = false;
    } catch (error) {
      console.error('Deletion error:', error.message || error);
    }
  }

  function cancelDelete() {
    showConfirmDelete = false;
  }

  // Function to get the product name by ID
  function getProductNameById(id) { 
    console.log("Searching for product with ID:", id); 
    console.log("Available products:", products); 
    const product = products.find(p => p.id === id); 
    if (!product) { console.error("Product not found for ID:", id); } 
    return product?.name || 'Unknown'; 
  }
</script>

<!-- Delete Button with Custom Design -->
<button
  type="button"
  class="button"
  on:click={openConfirmationDialog}
  disabled={selectedProducts.size === 0}
>
  <span class="button__text">Eliminar</span>
  <span class="button__icon">
    <svg xmlns="http://www.w3.org/2000/svg" width="512" viewBox="0 0 512 512" height="512" class="svg">
      <title>Delete Icon</title>
      <path
        style="fill:none;stroke:#323232;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
        d="M112,112l20,320c.95,18.49,14.4,32,32,32H348c17.67,0,30.87-13.51,32-32l20-320"
      ></path>
      <line
        y2="112"
        y1="112"
        x2="432"
        x1="80"
        style="stroke:#323232;stroke-linecap:round;stroke-miterlimit:10;stroke-width:32px"
      ></line>
      <path
        style="fill:none;stroke:#323232;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
        d="M192,112V72h0a23.93,23.93,0,0,1,24-24h80a23.93,23.93,0,0,1,24,24h0v40"
      ></path>
      <line
        y2="400"
        y1="176"
        x2="256"
        x1="256"
        style="fill:none;stroke:#323232;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
      ></line>
      <line
        y2="400"
        y1="176"
        x2="192"
        x1="184"
        style="fill:none;stroke:#323232;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
      ></line>
      <line
        y2="400"
        y1="176"
        x2="320"
        x1="328"
        style="fill:none;stroke:#323232;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
      ></line>
    </svg>
  </span>
</button>

{#if showAlert}
  <div class="alert">
    No hay productos seleccionados para eliminar.
  </div>
{/if}

{#if showConfirmDelete}
  <div class="popup-overlay">
    <div class="popup-content">
      <h3>¿Estás seguro de que quieres eliminar estos productos?</h3>
      <ul>
        {#each Array.from(selectedProducts) as productId}
          <li>Producto: {getProductNameById(productId)}</li>
        {/each}
      </ul>
      <div class="popup-actions">
        <button on:click={cancelDelete}>Cancelar</button>
        <button on:click={confirmDelete}>Eliminar</button>
      </div>
    </div>
  </div>
{/if}

<style>
  /* Styles for the custom button */
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
    padding: 0;
    outline: none;
    transition: background 0.3s, transform 0.1s, box-shadow 0.1s;
  }

  .button:disabled {
    cursor: not-allowed;
    opacity: 0.6;
  }

  .button, .button__icon, .button__text {
    transition: all 0.3s;
  }

  .button__text {
    transform: translateX(33px);
    color: var(--font-color);
    font-weight: 600;
    pointer-events: none;
  }

  .button__icon {
    position: absolute;
    transform: translateX(109px);
    height: 100%;
    width: 39px;
    background-color: var(--bg-color-sub);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .button__icon .svg {
    width: 20px;
    fill: var(--main-color);
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

  /* Styles for the alert */
  .alert {
    background-color: #f44336;
    color: white;
    padding: 10px;
    border-radius: 5px;
    margin-top: 10px;
    text-align: center;
  }

  /* Styles for the confirmation dialog */
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
  }

  .popup-content {
    background: #fff;
    padding: 20px 30px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
    text-align: center;
    max-width: 400px;
    width: 90%;
  }

  .popup-content h3 {
    margin-bottom: 15px;
    color: var(--font-color);
  }

  .popup-content ul {
    list-style-type: none;
    padding: 0;
    margin-bottom: 20px;
    text-align: left;
  }

  .popup-content li {
    margin-bottom: 5px;
    color: var(--font-color);
  }

  .popup-actions {
    display: flex;
    justify-content: flex-end;
  }

  .popup-actions button {
    margin: 5px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.3s;
  }

  .popup-actions button:first-child {
    background-color: #f4f4f4;
  }

  .popup-actions button:last-child {
    background-color: #cc0000;
    color: #fff;
  }

  .popup-actions button:first-child:hover {
    background-color: #e0e0e0;
  }

  .popup-actions button:last-child:hover {
    background-color: #b30000;
  }
</style>