import { createClient } from 'redis';


const client = createClient()
  .on('ready', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });


function publishMessage(message, time) {
  function func() {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }
  setTimeout(func, time);
}


publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
