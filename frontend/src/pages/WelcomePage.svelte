<script>
  import WelcomeButton from '../components/WelcomeButton.svelte';
  import { createEventDispatcher } from 'svelte';
  
  const dispatch = createEventDispatcher();
</script>

<div class="welcome-container">
  <div class="welcome-content">
    <h1 class="welcome-title">¡Bienvenido a la App para gestionar tu inventario!</h1>
    <div class="button-container">
      <WelcomeButton on:enter={() => dispatch('enter')} />
    </div>
  </div>
</div>

<style>
  .welcome-container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    text-align: center;
  }

  .welcome-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem; 
  }

  .welcome-title {
    margin: 0;
    font-size: 2rem;
    color: #333;
  }

  .button-container {
    display: flex;
    justify-content: center;
  }
</style>