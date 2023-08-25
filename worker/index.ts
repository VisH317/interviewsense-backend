import { Stripe } from 'stripe'

const stripe = new Stripe(Bun.env.STRIPE_SK as string, {
    apiVersion: "2023-08-16"
})

Bun.serve({
    port: 8000,
    fetch(req) {
        const url = new URL(req.url)
        if(url.pathname === "/") {
            console.log("stripe worker to be finished later")
        }
        return new Response("404")
    }
})