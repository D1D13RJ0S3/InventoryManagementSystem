<!--
Component: WelcomePage.svelte
Description: This component serves as the welcome page for the inventory management application.
It displays a welcome message and an animated button that dispatches an 'enter' event when clicked.
Properties:
  - None
Internal Variables:
  - dispatch (function): Dispatcher to emit custom events.
Main Functions:
  - None
External Dependencies:
  - WelcomeButton.svelte: Component that renders the welcome button.
  - createEventDispatcher from Svelte: Used for event communication between components.
-->
<script>
  // Import the WelcomeButton component from the components directory
  import WelcomeButton from '../components/FunctionPages/WelcomeButton.svelte';
  
  // Import createEventDispatcher from Svelte for communication between components
  import { createEventDispatcher } from 'svelte';
  
  // Create an event dispatcher
  const dispatch = createEventDispatcher();
</script>

<!-- Main welcome container -->
<div class="welcome-container">
  <div class="welcome-content">
    <!-- Welcome title -->
    <h1 class="welcome-title">¡Bienvenido a la App para gestionar tu inventario!</h1>
    <div class="button-container">
      <!-- WelcomeButton component that dispatches the 'enter' event -->
      <WelcomeButton on:enter={() => dispatch('enter')} />
    </div>
  </div>
</div>

<style>
  /* 
    Container that centers the welcome content both vertically and horizontally.
    Uses flexbox for alignment and occupies the full viewport height.
  */
  .welcome-container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    text-align: center;
  }

  /* 
    Centered welcome content.
    Arranges elements vertically with a small gap between them.
  */
  .welcome-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem; 
  }

  /* 
    Style for the welcome title.
    Removes default margin, sets font size and color.
  */
  .welcome-title {
    margin: 0;
    font-size: 2rem;
    color: #333;
  }

  /* 
    Container for the welcome button.
    Centers the button horizontally.
  */
  .button-container {
    display: flex;
    justify-content: center;
  }
</style>