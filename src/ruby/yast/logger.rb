require "yastx"
require "yast/builtins"

module Yast
  # @private
  module_function def y2_logger_helper(level, args)
    caller_frame = 1
    backtrace = false

    if args.first.is_a? Fixnum
      if args.first < 0
        backtrace = true
        args.shift
        caller_frame = 2
      else
        caller_frame += args.shift
      end
    end

    res = Builtins.sformat(*args)
    res.gsub!(/%/, "%%") # reescape all %
    caller[caller_frame] =~ /(.+):(\d+):in `([^']+)'/
    y2_logger(level, "Ruby", Regexp.last_match(1), Regexp.last_match(2).to_i, Regexp.last_match(3), res)

    if backtrace
      y2_logger_helper(level, [2, "------------- Backtrace begin -------------"])
      caller(3).each { |frame| y2_logger_helper(level, [4, frame]) }
      y2_logger_helper(level, [2, "------------- Backtrace end ---------------"])
    end
  end

  # write to log debug message with arguments formated by {Yast::Builtins.sformat}
  module_function def y2debug(*args)
    y2_logger_helper(0, args)
  end

  # write to log milestone message with arguments formated by {Yast::Builtins.sformat}
  module_function def y2milestone(*args)
    y2_logger_helper(1, args)
  end

  # write to log warning message with arguments formated by {Yast::Builtins.sformat}
  module_function def y2warning(*args)
    y2_logger_helper(2, args)
  end

  # write to log error message with arguments formated by {Yast::Builtins.sformat}
  module_function def y2error(*args)
    y2_logger_helper(3, args)
  end

  # write to log security message with arguments formated by {Yast::Builtins.sformat}
  # @todo make it clear what is supposed to write to this level
  module_function def y2security(*args)
    y2_logger_helper(4, args)
  end

  # write to log internal error message with arguments formated by {Yast::Builtins.sformat}
  module_function def y2internal(*args)
    y2_logger_helper(5, args)
  end
end # module YaST
