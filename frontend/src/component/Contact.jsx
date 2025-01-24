const Contact = () => {
  return (
    <div className="container mx-auto mt-[160px]">
      <h2 className="font-Allura text-[60px] text-[#343333] text-center">
        Get in Touch
      </h2>
      <form className="flex flex-col items-center mt-10">
        <input
          type="text"
          placeholder="Your Name"
          className="border border-[#EDEDED] rounded-[10px] px-5 py-3 w-[300px] mb-5"
        />
        <input
          type="email"
          placeholder="Your Email"
          className="border border-[#EDEDED] rounded-[10px] px-5 py-3 w-[300px] mb-5"
        />
        <textarea
          placeholder="Your Message"
          className="border border-[#EDEDED] rounded-[10px] px-5 py-3 w-[300px] h-[100px] mb-5"
        />
        <button
          type="submit"
          className="font-Akaya_Kanadaka text-white font-[26px] leading-[26px] bg-[#6246E4] px-16 py-5 rounded-[10px] hover:shadow-xl transition-all duration-150"
        >
          Send
        </button>
      </form>
    </div>
  );
};

export default Contact;
