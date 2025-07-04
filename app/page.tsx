export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-white text-gray-800 p-8">
      <h1 className="text-4xl font-bold mb-4">OrganicNews</h1>
      <p className="text-lg mb-6 text-center max-w-xl">
        Daily articles based on the latest scientific studies about nature, health, and the human body. 100% free and understandable.
      </p>
      <a
        href="#"
        className="bg-green-600 text-white px-6 py-3 rounded-full shadow hover:bg-green-700 transition"
      >
        Start Learning now
      </a>
    </main>
  );
}