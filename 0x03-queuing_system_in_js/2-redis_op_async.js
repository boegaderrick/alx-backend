import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient()
  .on('ready', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    if (error) {
      console.log(error);
    } else {
      print(`Reply: ${reply}`);
    }
    //client.quit();
  });
}

async function displaySchoolValue(schoolName) {
  const get = promisify(client.get).bind(client);
  const func = async () => {
    const value = await get(schoolName);
    console.log(value);
  }
  await func();
}

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

main();
