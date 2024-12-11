<!--
Component: WelcomeButton.svelte
Description: This component renders an animated button that dispatches an 'enter' event when clicked.
Properties:
  - None
Internal Variables:
  - dispatch (function): Dispatcher to emit custom events.
Main Functions:
  - handleClick(): Handles button click and dispatches the 'enter' event.
External Dependencies:
  - createEventDispatcher from Svelte: Used for event communication between components.
-->
<script>
  // Import createEventDispatcher from Svelte to handle communication between components
  import { createEventDispatcher } from 'svelte';
  
  // Create an event dispatcher for handling custom events
  const dispatch = createEventDispatcher();
    
  /**
   * Handles the button click and dispatches the 'enter' event.
   */
  function handleClick() {
    dispatch('enter'); 
  }
</script>
  
<!-- Main container for the welcome button -->
<div class="welcome-container">
  <!-- Animated button to enter the application -->
  <button class="animated-button" on:click={handleClick}>
    Enter
  </button>
</div>
  
<style>
  /* 
    Styles for the button.
    Removes default appearance, sets border, border-radius, box-sizing, color, cursor, and display properties.
    Defines font properties, size, weight, and adds transitions for interactive states.
  */
  button {
    appearance: none;
    background-color: transparent;
    border: 0.125em solid #1A1A1A;
    border-radius: 0.9375em;
    box-sizing: border-box;
    color: #3B3B3B;
    cursor: pointer;
    display: inline-block;
    font-family: Roobert, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-size: 16px;
    font-weight: 600;
    line-height: normal;
    margin: 0;
    min-height: 3.75em;
    min-width: 0;
    outline: none;
    padding: 1em 2.3em;
    text-align: center;
    text-decoration: none;
    transition: all 300ms cubic-bezier(.23, 1, 0.32, 1);
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    will-change: transform;
  }

  /* 
    Styles for the disabled state of the button.
    Disables pointer events to prevent interaction.
  */
  button:disabled {
    pointer-events: none;
  }

  /* 
    Styles for the button in hover state.
    Changes text color, background color, adds box-shadow, and applies a translation for a lifting effect.
  */
  button:hover {
    color: #fff;
    background-color: #1A1A1A;
    box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
    transform: translateY(-2px);
  }

  /* 
    Styles for the button in active state.
    Removes box-shadow and resets the translation to original position.
  */
  button:active {
    box-shadow: none;
    transform: translateY(0);
  }
</style>