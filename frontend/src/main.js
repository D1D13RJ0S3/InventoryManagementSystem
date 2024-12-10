/**
 * main.js
 * Description: Entry point for the Svelte application. It imports the main App component,
 * initializes it, and optionally tests the accessibility of the fetchProducts function.
 * 
 * External Dependencies:
 * - App.svelte: The root Svelte component for the application.
 * - fetchProducts (from ./lib/api.js): Function to fetch products data from the API.
 */

import App from './App.svelte';
import { fetchProducts } from './lib/api.js';

// Optionally, test if the fetchProducts function is accessible
fetchProducts()
  .then(console.log)
  .catch(console.error);

/**
 * Initializes the Svelte application by mounting the App component to the document body.
 * Passes initial props to the App component.
 */
const app = new App({
  target: document.body,
  props: {
    name: 'world' // Example prop passed to the App component
  }
});

// Export the app instance for potential further manipulation or testing
export default app;