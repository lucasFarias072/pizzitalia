function createBillCard(billValue) {
  const billBanner = document.createElement('span')
  billBanner.style.backgroundColor = 'rgb(128, 255, 128)'
  billBanner.style.border = 'solid 1px #222'
  billBanner.style.borderRadius = '.5rem'
  billBanner.style.margin = '0 1rem'
  billBanner.style.padding = '.2rem 1rem'
  billBanner.textContent = `R$ ${billValue}`
  return billBanner 
}

document.addEventListener('DOMContentLoaded', function() {
  const costumerId = document.getElementById('costumer_id')
  
  const allCostumers = [...document.querySelectorAll('.costumer')]
  const allCategories = [...document.querySelectorAll('.cat')]
  const allSizes = [...document.querySelectorAll('.pizza-size')]
  
  const pizzaTypes = document.getElementById('pizza-types')
  const pizzaSizes = document.getElementById('pizza-sizes')
  const pizzaPrices = document.getElementById('pizza-prices')
  
  const pizzaAverage = document.getElementById('pizza-average')
  const pizzaLarge = document.getElementById('pizza-large')
  const pizzaLarger = document.getElementById('pizza-larger')

  const calculateOrder = document.getElementById('calculate-order')
  const pricesTable = document.getElementById('prices-table')

  let bill = 0
  
  console.log(allCostumers)
  console.log(allCategories)
  
  // -------------------------------------------------------------------------------- IMPORTANT INPUTS
  allCategories.forEach(cat => {
    // console.log(cat.childNodes[1].textContent) // signature
    // console.log(cat.childNodes[3].textContent) // label
    // console.log(cat.childNodes[5].textContent.split('/')) // prices [0, 1, 2]
    
    cat.addEventListener("click", () => {
      pizzaTypes.value += cat.childNodes[1].textContent + '.'
      const pricesForThisPizza = cat.childNodes[5].textContent.split("/")
      
      const thisPizzaAveragePrice = document.createElement('span')
      const thisPizzaLargePrice = document.createElement('span')
      const thisPizzaLargerPrice = document.createElement('span')
      
      // Showing each price of each pizza based on category
      thisPizzaAveragePrice.textContent = pricesForThisPizza[0]
      thisPizzaLargePrice.textContent = pricesForThisPizza[1]
      thisPizzaLargerPrice.textContent = pricesForThisPizza[2]
      
      // todo: Give each price of a pizza, their style
      thisPizzaAveragePrice.classList.add('price-style')
      thisPizzaLargePrice.classList.add('price-style')
      thisPizzaLargerPrice.classList.add('price-style')

      thisPizzaAveragePrice.classList.add('pizza-average')
      thisPizzaLargePrice.classList.add('pizza-large')
      thisPizzaLargerPrice.classList.add('pizza-larger')
      
      thisPizzaAveragePrice.addEventListener('click', () => {
        pizzaPrices.value += thisPizzaAveragePrice.textContent + "/"
        pricesTable.innerHTML = ""
      })
      thisPizzaLargePrice.addEventListener('click', () => {
        pizzaPrices.value += thisPizzaLargePrice.textContent + "/"
        pricesTable.innerHTML = ""
      })
      thisPizzaLargerPrice.addEventListener('click', () => {
        pizzaPrices.value += thisPizzaLargerPrice.textContent + "/"
        pricesTable.innerHTML = ""
      })
      pricesTable.appendChild(thisPizzaAveragePrice)
      pricesTable.appendChild(thisPizzaLargePrice)
      pricesTable.appendChild(thisPizzaLargerPrice)
      // pizzaPrices.value += pricesForThisPizza
    })
  })

  allSizes.forEach(size => {
    size.addEventListener("click", () => {
      pizzaSizes.value += size.textContent + '.'
    })
  })
  // ------------------------------------------------------------------------------------------------

  calculateOrder.addEventListener('click', () => {
    const ordersInputs = pizzaPrices.value.split('/')
    for(let i = 0; i < ordersInputs.length; i++) {
      if (ordersInputs[i] != '') {
        bill += parseFloat(ordersInputs[i])
      }
    }
    
    const billBanner = createBillCard(bill)
    document.getElementById('stats').appendChild(billBanner)
    calculateOrder.setAttribute('disabled', '')
    
    // const billBanner = document.createElement('span')
    // billBanner.classList.add('price-style')
    // billBanner.textContent = `Valor a pagar: R$ ${bill}`
    // pricesTable.appendChild(billBanner)
    
    // todo: Capture each data to be sent to the backend
    document.getElementById('enable-order').classList.remove('vanished')
    document.getElementById('orders_list').value = pizzaTypes.value
    document.getElementById('sizes_list').value = pizzaSizes.value
    document.getElementById('order_bill').value = bill
    // 'client_owner is gotten on html'
  })

  const loop = setInterval(() => {
    // console.log(costumerId.value)
    console.log('qtd. pizzas: ', pizzaTypes.value.split(".").length)
    console.log('tamanhos: ', pizzaSizes.value.split(".").length)

    if (costumerId.value != '') {
      allCostumers.forEach(costumer => {
        if (costumer.textContent[0] === costumerId.value[0]) {
          costumer.classList.remove('vanished')
          costumer.classList.add('query-beauty')
        }
      })
    } else {
      allCostumers.forEach(costumer => {
        if (!costumer.getAttribute('class').includes('vanished')) {
          costumer.classList.add('vanished')
        }
      })
    }
    
  }, 1000)
});
