+++
title = 'Contacto'
draft = false
+++

<div class="contact-info">
  <div class="contact-item">
    <a href="https://wa.me/34677357892" target="_blank" rel="noopener noreferrer" class="icon-link">
      {{< figure src="/images/whatsapp-svgrepo-com.svg" width="100" height="100" alt="WhatsApp" class="contact-icon" >}}
    </a>
    <p class="contact-text">+34 677 357 892</p>
  </div>
  <div class="contact-item">
    <a href="mailto:vidal.mariaflorencia2@gmail.com" target="_blank" rel="noopener noreferrer" class="icon-link">
      {{< figure src="/images/gmail-svgrepo-com.svg" width="90" height="90" alt="Email" class="contact-icon" >}}
    </a>
    <p class="contact-text">vidal.mariaflorencia2@gmail.com</p>
  </div>
</div>

<style>
  .contact-info {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 40px; /* Space between the two contact items */
    margin: 20px 0; /* Vertical margin, adjust as needed */
  }

  .contact-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .icon-link {
    display: block;
    margin-bottom: 10px; /* Space between icon and text */
  }

  .contact-icon {
    width: 50px;
    height: 50px;
  }

  .contact-text {
    margin: 0;
    font-size: 1em; /* Adjust as needed */
  }
</style>