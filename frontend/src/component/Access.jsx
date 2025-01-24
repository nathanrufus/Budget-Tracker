const Access = () => {
  return (
    <div className="container mx-auto mt-[160px]">
      <h2 className="font-Allura text-[60px] text-[#343333] text-center">
        Sign Up for Early Access
      </h2>
      <form className="flex flex-col items-center mt-10">
        <input
          type="email"
          placeholder="Enter your email"
          className="border border-[#EDEDED] rounded-[10px] px-5 py-3 w-[300px] mb-5"
        />
        <button
          type="submit"
          className="font-Akaya_Kanadaka text-white font-[26px] leading-[26px] bg-[#6246E4] px-16 py-5 rounded-[10px] hover:shadow-xl transition-all duration-150"
        >
          Sign Up
        </button>
      </form>
    </div>
  );
};

export default Access;
