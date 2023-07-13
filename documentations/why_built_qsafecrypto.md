## Why I built and use QSafeCrypto, and why you should use it

I was coding for my startup, Mindread.io. I was storing the data in key-value pairs in memory to get the fastest possible results. I received the data in JSON format and stored it as a single string after stringifying it. As a SaaS, I don't have the luxury of sending user data to other vendor-provided databases that are encrypted at rest. I have to do it myself. I felt the need to encrypt and decrypt user data. So, how could I encrypt and decrypt it? I started by searching Google for best practices.

There is a simple approach: encrypt it with a key, and then decrypt it with the same key. However, I came across a talk by an industry veteran who urged everyone to use quantum-safe encryption to store user data, especially important data. Why? Because in 4-5 years, quantum computers will be able to crack these encryption methods.

I thought, "That's not my problem." There's a term in chess: "Never defend your pieces early against possible attacks." So, it will happen in 4-5 years, and then I'll re-encrypt everything.

Then, he dropped another bombshell. He said that big hackers are collecting encrypted data in the air and hoarding it en masse. They believe that once quantum computers can crack it, they will be able to see the data. Many data sets will not become stale and will remain relevant. For example, a customer's name, gender, age, and email address. These data sets could be leaked and pose a serious threat.

Hmmm... That's pretty concerning. So, what should we do? The protagonist then said, "Just start implementing quantum-safe encryption from now on. It's the safest bet."

So, I started researching how to implement quantum-safe encryption. First, I had to find which encryption algorithms are safe from quantum attack. I found a debatable list. NIST has not yet released an official list, but researchers have found a few that are relatively safe.

However, I found it very challenging to use existing solutions. Extensive theoretical knowledge was required, and another popular solution, Pycryptodome, also had its complications.

During my research, I discovered the Google TINK cryptography library, which was incredibly helpful. However, it still involved substantial theoretical understanding and installation hurdles. Additionally, there was a potential vendor lock-in risk. Most of the time, developers had to be knowledgeable about what they were doing and not "shoot themselves in the foot." Finally, I made the difficult decision to build QSafeCrypto from scratch. After a long research and reading a gazillion amount of internet resources and Stack Overflow questions, I finally implemented it.

Since then, the library has been used in production and has successfully encrypted millions of megabytes of data with lower latency and improved ease of use. Now, as a time-tested program, I wanted to make it open source.

As I am working with a team, lecturing CS theories like proper nonce and associated tag bytes to make them understand the thing seems difficult. So, I wrapped everything in a simple package and told them to just use the encrypt() and decrypt() functions.

I had four requirements for developing it. I followed them religiously.

1. The library must include two functions: one for encryption and another for decryption.
2. A key will be necessary, stored either in the environment variable or in the Key Management System (KMS), which will be used for encryption and decryption.
3. The library must be performant and quantum-safe.
4. It should be designed in a way that even developers cannot easily make errors. Additionally, the encrypted keys should have an aesthetically pleasing appearance.

I chose AES-GCM-256 for five reasons as well:

1. It's never been cracked yet.
2. Companies like Signal are using it in their chatting app. Google's Tink library also chooses this algorithm. Big tech are 3. already using it. There is enough social proof.
3. It's fast because there is chip-level support provided by major vendors for this particular algorithm.
4. There is already a supporting Python library with first-class support.
5. It's quantum-safe.

Use it to get quantum-safe encryption and decryption from today, easily.