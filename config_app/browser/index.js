(async () => {
    const browser = await puppeteer.launch({
      headless: false,
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox'
      ],
    });
    const page = await browser.newPage();
    await page.goto(`http://localhost:${port}`);
  })();
  